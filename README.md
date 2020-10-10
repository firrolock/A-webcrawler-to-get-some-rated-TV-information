# A-webcrawler-to-get-some-rated-TV-information
The module "analyse_str" can be used to get rid of odd spaces in a string, not only for this crawler program. Feel free to take and invoke that if you need in a program.
本程序用python爬取时光网电视剧TOP100的数据，附加一个字符串解析处理模块。

电视剧数据包含剧名、导演、主演和简介4个部分。

程序运用多协程爬取数据和存储数据，同时使用gevent库中的queue模块，建立两个数据队列，一个queue_url用来存储待爬取的网页url，一个queue_data存储将要写入文件的字符串列表。由于本次爬取的时光网电视剧页面url总共有10个，所以将queue_url队列中数据个数限定为10，queue_data中的字符串列表个数不确定，所以没有进行限定。

程序运行前需要安装gevent, requests, bs4库/模块，可在终端使用"pip install 库/模块名"来安装。中国大陆用"pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 库/模块名"下载速度能快些。

程序包含"tv_list.py"和"analyse_str.py"两个文件，运行时两个文件需要在同一个文件夹。程序入口是"tv_list.py", 里面引用了"analyse_str"模块用来解析处理从网页里获取到的信息，主要为了去掉换行符、制表符以及多余的空格等。

我编写的"analyse_str"模块可以将字符串中所有中间的换行符和制表符都替换为空格符，最后面的会直接删去；考虑到英文单词正常空格以及某些需要空的地方，处理空格符从3个连续空格开始处理，当然字符串最前面的空格或换行符或制表符不管是一个还是很多个都会被去除，在字符串中间能处理的最大连续空格数是7个，将每处3-7个连续空格符替换为2个连续空格符，处于最后面的直接删去不替换。这个模块如果有需要可以引用在其他程序里。

爬取网站存在不确定因素，大部分电视剧有剧名、导演、主演和简介这四个信息，而有的只有剧名和主演信息，有的又只有剧名和简介信息，如此之类。因此存储进csv文件中的某些行数据会不全。在程序里应用了异常处理机制，即便有的信息不全，也保证程序可以运行下去，将存在的所有信息都存储下来。
