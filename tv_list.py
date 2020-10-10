from gevent import monkey, queue
monkey.patch_all();
from analyse_str import get_str
import gevent, requests, bs4, csv, time, os
queue_url = queue.Queue(10);  #string
queue_data = queue.Queue();  #string list
#monkey.patch_all();  #tv_list.py:4: MonkeyPatchWarning: Monkey-patching ssl after ssl has already been imported may lead to errors, including RecursionError on Python 3.6. It may also silently lead to incorrect behaviour on Python 3.7. Please monkey-patch earlier. See https://github.com/gevent/gevent/issues/1016. Modules that had direct imports (NOT patched): ['urllib3.util (C:\\Users\\Firrolock\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\urllib3\\util\\__init__.py)', 'urllib3.util.ssl_ (C:\\Users\\Firrolock\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\urllib3\\util\\ssl_.py)'].
#1: http://www.mtime.com/top/tv/top100/ 2-10: http://www.mtime.com/top/tv/top100/index-2.html

def save_data(num):
    title = ["TV Name", "Directors", "Actors/Actresses", "Introductions"];
    #print("***save data gevent num: %d."%num);
    if not os.path.exists("./tv_list.csv"):
        f = open("tv_list.csv", "w", newline = "", encoding = "utf-8");
        writer = csv.writer(f);
        writer.writerow(title);
        f.close();
    f = open("tv_list.csv", "a", newline = "", encoding = "utf-8");
    writer = csv.writer(f);
    while not queue_data.empty():
        writer.writerow(queue_data.get_nowait());
    f.close();

def queue_push():
    url = "http://www.mtime.com/top/tv/top100/";
    queue_url.put_nowait(url);
    for page in range(2,11):
        if not queue_url.full():
            queue_url.put_nowait("http://www.mtime.com/top/tv/top100/index-%d.html"%page);

def dispatch(func):
    work_list = [];
    for x in range(3):
        work_list.append(gevent.spawn(func, x + 1));
    gevent.joinall(work_list);

def crawler(num):
    headers = {
    "Referer": "http://www.mtime.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    };
    #print("***crawler gevent num: %d."%num);
    while not queue_url.empty():
        res = requests.get(queue_url.get_nowait(), headers = headers);
        #print("response encoding: {}.".format(res.encoding));
        #res.encoding = "utf-8";
        try:
            soup = bs4.BeautifulSoup(res.text, "html.parser");
            info_all = soup.find_all("div", class_ = "mov_con");
        except Exception as e:
            print(e);
            continue;
        for info in info_all:
            list_info = [];
            try:
                list_info.append(get_str(info.find("h2").text));
                list_info.append(get_str(info.find("p").text));
                list_info.append(get_str(info.find_all("p")[1].text));
                list_info.append(get_str(info.find_all("p")[2].text));
                # list_info.append(info.find("h2").text);
                # list_info.append(info.find("p").text);
                # list_info.append(info.find_all("p")[1].text);
                # list_info.append(info.find_all("p")[2].text);
            except Exception as e:
                #print("get partial tv info: ", end = "");
                #print(e);
                pass;
            queue_data.put_nowait(list_info);
        dispatch(save_data);
        time.sleep(1);


if __name__ == "__main__":
    time_start = time.time();
    print("job start...");
    queue_push();
    dispatch(crawler);
    print("job done...");
    print("time spent: ", end = "");
    print(time.time() - time_start);


