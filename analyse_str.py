#This module can be used to analyse and get rid of odd spaces of some string either in a webcrawler program or other programs if needed.

#Deal with every sign of "\n", "\t" or "\v" in target string with recursive method.
def trunc_str(string_src):
    for i in range(len(string_src)):
        if string_src[i] == "\n" or string_src[i] == "\t" or string_src[i] == "\v":
            break;
    else:
        return string_src;
    for i in range(len(string_src)):
        if string_src[i] == "\n" or string_src[i] == "\t" or string_src[i] == "\v":
            if i + 1 < len(string_src):
                return trunc_str(string_src[:i]) + " " + trunc_str(string_src[i + 1:]);
            else:
                return trunc_str(string_src[:i]);

#Deal with space signs. The largest continuous spaces this function may handle is 7.
def trunc_str2(string_src):
    for i in range(len(string_src)):
        if string_src[i] == " " and i + 3 <= len(string_src) and (string_src[i: i + 3] == "   " or i + 4 <= len(string_src) and (string_src[i: i + 4] == "    " or i + 5 <= len(string_src) and (string_src[i: i + 5] == "     " or i + 6 <= len(string_src) and (string_src[i: i + 6] == "      " or i + 7 <= len(string_src) and string_src[i: i + 7] == "       ")))):
            break;
    else:
        return string_src;
    for i in range(len(string_src)):
        if string_src[i] == " " and i + 3 <= len(string_src) and string_src[i: i + 3] == "   ":
            if i + 7 <= len(string_src) and string_src[i: i + 7] == "       ":
                if i + 7 < len(string_src):
                    return trunc_str2(string_src[:i]) + "  " + trunc_str2(string_src[i + 7:]);
                else:
                    return trunc_str2(string_src[:i]);
            elif i + 6 <= len(string_src) and string_src[i: i + 6] == "      ":
                if i + 6 < len(string_src):
                    return trunc_str2(string_src[:i]) + "  " + trunc_str2(string_src[i + 6:]);
                else:
                    return trunc_str2(string_src[:i]);
            elif i + 5 <= len(string_src) and string_src[i: i + 5] == "     ":
                if i + 5 < len(string_src):
                    return trunc_str2(string_src[:i]) + "  " + trunc_str2(string_src[i + 5:]);
                else:
                    return trunc_str2(string_src[:i]);
            elif i + 4 <= len(string_src) and string_src[i: i + 4] == "    ":
                if i + 4 < len(string_src):
                    return trunc_str2(string_src[:i]) + "  " + trunc_str2(string_src[i + 4:]);
                else:
                    return trunc_str2(string_src[:i]);
            else:
                if i + 3 < len(string_src):
                    return trunc_str2(string_src[:i]) + "  " + trunc_str2(string_src[i + 3:]);
                else:
                    return trunc_str2(string_src[:i]);

#Deal with odd spaces in front or end of the target string.                
def cut_str(string_src):
    head = 0;
    tail = 0;
    for i in string_src:
        if i == " " or i == "\n" or i == "\t" or i == "\v":
            head += 1;
        else:
            break;
    cnt = head + 1;
    for i in string_src[head + 1:]:
        if i != " " and i != "\n" and i != "\t" and i != "\v":
            pass;
        elif cnt + 1 < len(string_src) and string_src[cnt + 1] != " " and string_src[cnt + 1] != "\n" and string_src[cnt + 1] != "\t" and string_src[cnt + 1] != "\v":
            pass;
        elif cnt + 2 < len(string_src) and string_src[cnt + 2] != " " and string_src[cnt + 2] != "\n" and string_src[cnt + 2] != "\t" and string_src[cnt + 2] != "\v":
            pass;
        elif cnt + 3 < len(string_src) and string_src[cnt + 3] != " " and string_src[cnt + 3] != "\n" and string_src[cnt + 3] != "\t" and string_src[cnt + 3] != "\v":
            pass;
        elif cnt + 4 < len(string_src) and string_src[cnt + 4] != " " and string_src[cnt + 4] != "\n" and string_src[cnt + 4] != "\t" and string_src[cnt + 4] != "\v":
            pass;
        elif cnt + 5 < len(string_src) and string_src[cnt + 5] != " " and string_src[cnt + 5] != "\n" and string_src[cnt + 5] != "\t" and string_src[cnt + 5] != "\v":
            pass;
        else:
            tail += 1;
        cnt += 1;
    #print("head: ", head);
    #print("tail: ", tail);
    if tail == 0:
        string_dest = string_src[head:];
    else:
        string_dest = string_src[head:-tail];
    return string_dest;

#Combine each of functions above to get final string.
def get_str(string_src):
    string_tmp = trunc_str(string_src);
    string_tmp = trunc_str2(string_tmp);
    string_dest = cut_str(string_tmp);
    return string_dest;

#Program entrance(just for some tests)
if __name__ == "__main__":
    print("test different method to get string.");
        #while (string = input("enter a string(quit to stop test): ")) != "quit":  #SyntaxError: invalid syntax
    string = input("enter a string: ");
    while string != "quit":
        print("1. " + cut_str(string));
        print("2. " + trunc_str(string));
        print("3. " + trunc_str2(string));
        print("4. " + trunc_str(cut_str(string)));
        print("4. " + cut_str(trunc_str(string)));
        print("5. " + trunc_str2(cut_str(string)));
        print("5. " + cut_str(trunc_str2(string)));  #transform from No. 5
        print("6. " + trunc_str2(trunc_str(string)));
        print("6. " + trunc_str(trunc_str2(string)));
        print("7. " + get_str(string));
        string = input("enter a string(quit to stop test): ");

#test result:
# C:\Users\Firrolock\codes>sublime_text analyse_str.py

# C:\Users\Firrolock\codes>python analyse_str.py
#   File "analyse_str.py", line 90
#     while (string = input("enter a string(quit to stop test): ")) != "quit":
#                   ^
# SyntaxError: invalid syntax

# C:\Users\Firrolock\codes>python analyse_str.py

# C:\Users\Firrolock\codes>python analyse_str.py
# test different method to get string.
# enter a string: hello world
# hello world
# hello world
# hello world
# hello world
# hello world
# hello world
# hello world
# enter a string(quit to stop test): quit

# C:\Users\Firrolock\codes>python analyse_str.py
# test different method to get string.
# enter a string: hello world
# 1. hello world
# 2. hello world
# 3. hello world
# 4. hello world
# 5. hello world
# 6. hello world
# 7. hello world
# enter a string(quit to stop test): hello world   ...
# 1. hello world   ...
# 2. hello world   ...
# 3. hello world  ...
# 4. hello world   ...
# 5. hello world  ...
# 6. hello world  ...
# 7. hello world  ...
# enter a string(quit to stop test):  fantastic   wow    ...
# 1. fantastic   wow    ...
# 2.  fantastic   wow    ...
# 3.  fantastic  wow  ...
# 4. fantastic   wow    ...
# 5. fantastic  wow  ...
# 6.  fantastic  wow  ...
# 7. fantastic  wow  ...
# enter a string(quit to stop test): fantastic   wow    ...
# 1. fantastic   wow    ...
# 2. fantastic   wow    ...
# 3. fantastic  wow  ...
# 4. fantastic   wow    ...
# 5. fantastic  wow  ...
# 6. fantastic  wow  ...
# 7. fantastic  wow  ...
# enter a string(quit to stop test): wow      wow
# 1. wow      wo
# 2. wow      wow
# 3. wow  wow
# 4. wow      wo
# 5. wow  wo
# 6. wow  wow
# 7. wow  wo
# enter a string(quit to stop test): wow     wow
# 1. wow     wow
# 2. wow     wow
# 3. wow  wow
# 4. wow     wow
# 5. wow  wow
# 6. wow  wow
# 7. wow  wow
# enter a string(quit to stop test): quit

# C:\Users\Firrolock\codes>python analyse_str.py
# test different method to get string.
# enter a string: wow       wow
# 1. wow       w
# 2. wow       wow
# 3. wow  wow
# 4. wow       w
# 5. wow  w
# 6. wow  wow
# 7. wow  w
# 8. wow  wow
# enter a string(quit to stop test): wow       wow
# 1. wow       w
# 2. wow       wow
# 3. wow  wow
# 4. wow       w
# 5. wow  w
# 6. wow  wow
# 7. wow  w
# 8. wow  wow
# enter a string(quit to stop test): wow        wow
# 1. wow
# 2. wow        wow
# 3. wow   wow
# 4. wow
# 5. wow
# 6. wow   wow
# 7. wow
# 8. wow   wow
# enter a string(quit to stop test): wow            wow
# 1. wow
# 2. wow            wow
# 3. wow    wow
# 4. wow
# 5. wow
# 6. wow    wow
# 7. wow
# 8. wow    wow
# enter a string(quit to stop test): wow   wow
# 1. wow   wow
# 2. wow  wow
# 3. wow   wow
# 4. wow  wow
# 5. wow   wow
# 6. wow  wow
# 7. wow  wow
# 8. wow   wow
# enter a string(quit to stop test): wow                  wow
# 1. wow                  wow
# 2. wow   wow
# 3. wow                  wow
# 4. wow   wow
# 5. wow                  wow
# 6. wow  wow
# 7. wow  wow
# 8. wow                  wow
# enter a string(quit to stop test): quit

# C:\Users\Firrolock\codes>python analyse_str.py
# test different method to get string.
# enter a string: wow       wow
# 1. wow       w
# 2. wow       wow
# 3. wow  wow
# 4. wow       w
# 5. wow  w
# 6. wow  wow
# 7. wow  wow
# 8. wow  wow
# enter a string(quit to stop test): start   mid          end
# 1. start   mid          end
# 2. start   mid   end
# 3. start  mid           end
# 4. start   mid   end
# 5. start  mid           end
# 6. start  mid  end
# 7. start  mid  end
# 8. start  mid           end
# enter a string(quit to stop test): quit

# C:\Users\Firrolock\codes>python analyse_str.py
# test different method to get string.
# enter a string:                 start   mid             end
# 1. start   mid          end
# 2.       start   mid   end
# 3.              start  mid              end
# 4. start   mid   end
# 4. start   mid   end
# 5. start  mid           end
# 5. start  mid           end
# 6.   start  mid  end
# 6.     start  mid   end
# 7. start  mid  end
# enter a string(quit to stop test):                  start   mid                 end
# 1. start   mid          end
# 2.         start   mid   end
# 3.                start  mid            end
# 4. start   mid   end
# 4. start   mid   end
# 5. start  mid           end
# 5. start  mid           end
# 6.    start  mid  end
# 6.       start  mid   end
# 7. start  mid  end
# enter a string(quit to stop test):   start       mid            end
# 1. start       mid              e
# 2.   start       mid   end
# 3.   start  mid                 end
# 4. start       mid   e
# 4. start       mid   e
# 5. start  mid           e
# 5. start  mid           end
# 6.   start  mid  end
# 6.   start  mid   end
# 7. start  mid  end
# enter a string(quit to stop test): quit

# C:\Users\Firrolock\codes>

