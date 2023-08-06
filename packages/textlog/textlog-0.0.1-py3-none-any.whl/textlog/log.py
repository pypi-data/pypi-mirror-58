import os
import sys
from datetime import datetime

def log(file_name, context, path=None, isPrint=False):
    if path is None:
        path = os.path.dirname(os.path.abspath("./")).replace("\\","/") + "/"
    else:
        path = path.replace("\\","/")
        if path[-1] != "/":
            path = path + "/"
    file_ = path + file_name + ".log"
    now = datetime.now()
    str_ = now.strftime('%Y-%m-%d %H:%M:%S') + " > " + context + "\n"
    try:
        with open(file_, "a") as myfile:
            myfile.write(str_)
    except:
        pass
    if isPrint is True:
        print(str_)

def help():
    print("log command list")
    print(" add")
    print("\t python log.py add file_name context")
    print("\t add option list")
    print("\t\t-p :: Write and print at same time.")
    print("\t\t-P :: Specifies the path of the file.")
    print("\t example")
    print('\t\tpython log.py add log "(2019.10.20 20:23) process >> END"')
    print('\t\tpython log.py add log "(2019.10.20 20:23) process >> END" -p')
    print('\t\tpython log.py add -P "c:/" log "(2019.10.20 20:23) process >> END" -p')
    print('\t\tpython log.py add -P "c:" log "(2019.10.20 20:23) process >> END" -p')
    print(" help")
    print("\t example")
    print('\t\tpython log.py help')

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) > 1:
        if "add" in argv:
            del argv[argv.index("add")]
            isPrint = False
            path = None
            if "-p" in argv:
                isPrint = True
                del argv[argv.index("-p")]
            if "-P" in argv:
                idx = argv.index("-P")
                path = argv[idx+1]
                del argv[idx]
                del argv[idx]
            if len(argv) == 3:
                log(argv[1], argv[2], path, isPrint)
            else:
                help()
        elif "help" in argv:
            help()
        else:
            help()
    else:
        help()
    