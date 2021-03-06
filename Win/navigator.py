import os
import argparse
import sys
import re
from termcolor import colored
from subprocess import call

'''
<Senthil360 @xda-developers.com>
This is basically a windows cmdline navigator written in python
Run the script, it should be self-explanatory
If it is a file it will be executed by the default program specified
If it is a directory it will be accessed
Might add Batch copy, move. delete in the future
'''

os.chdir("D://codes")

def movebase(input):
    d = ('{}://'.format(optbase))
    os.chdir(d)
    if checkaccess("d"):
        print(os.listdir(os.getcwd()))
    if checkaccess("f"):
        print((os.listdir(os.getcwd())))


def checkaccess(acc):                            #Open in directory only or files only mode
    if len(sys.argv) == 1:
        return True
    if sys.argv[1] == acc:
        return True

def favdir():
    with open("D://codes//Windows//often.txt", 'r') as e:   # Your file with locations
        f = 1
        favlist = []
        for line in e:
            dis = ('{} - {}'.format(f, line))
            print(colored(dis, 'magenta'))
            f = f + 1
            favlist.append(line.replace("\n", ""))
        return favlist


def space():
    print("")
    print("============")
    print("")


while True:
    space()
    print(colored(os.getcwd(), 'yellow'))
    space()
    a = 1
    dirlist = []
    for i in (os.listdir(os.getcwd())):
        call(["clear"])
        if os.path.isdir(i):
            if checkaccess("d") or checkaccess("all"):
                dis = ('{} - {}'.format(a, i))
                print(colored(dis, 'red'))
                del dis
                a = a + 1
        elif os.path.isfile(i):
            if checkaccess("f") or checkaccess("all"):
                dis =('{} - {}'.format(a,i))
                print(colored(dis, 'green'))
                del dis
                a = a + 1
        dirlist.append(i)
    space()
    print(colored('1 - {}'.format(int(a)-1), 'yellow'), " - select file/dir")
    print("        or       ")
    print(colored("base ", 'yellow'), " - change to a root drive")
    print("        or       ")
    print(colored("fol ", 'yellow'), " - Access directory list")
    print("        or       ")
    print(colored("prev", 'yellow'), " - parent directory")
    space()
    opt = input("Option : ")
    print(opt)

    if opt == 'base':
        optbase = input(" Choose C, D or h")
        movebase(optbase)
        del opt
    elif opt == 'fol':
        call(["clear"])
        favdir()
        optfav = input(" Choose a directory ")
        os.chdir(favdir()[int(int(optfav)-1)])
        print(os.getcwd())
        del opt
    elif opt == "view":
        call(["clear"])
        print("Under Construction")
#       v = int(viewno) - 1
#       print(os.stat(dirlist[int(v)]))
        del opt
    elif opt == "prev":
        call(["clear"])
        os.chdir('..')
        del opt
    elif opt == 'br':
        optbring = input("Choose file/dir : ")
        if os.path.isfile(dirlist[int(int(optbring)-1)]):
            os.startfile(dirlist[int(int(optbring)-1)])
        elif os.path.isdir(dirlist[int(int(optbring)-1)]):
            os.startfile(dirlist[int(int(optbring)-1)])
        del opt
    else:
        if os.path.isfile(dirlist[int(int(opt)-1)]):
            os.startfile(dirlist[int(int(opt)-1)])
            del opt
        elif os.path.isdir(dirlist[int(int(opt)-1)]):
            call(["clear"])
            os.chdir(dirlist[int(int(opt)-1)])
            os.listdir(os.getcwd())
            del opt
