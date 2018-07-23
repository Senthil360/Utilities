import os
import argparse
import sys
import re
from termcolor import colored

'''
This is basically a windows cmdline navigator written in python
Run the script, it should be self-explanatory
If it is a file it will be executed by the default program specified
If it is a directory it will be accessed
Might add Batch copy, move. delete in the future
'''


def movebase(input):
    d = ('{}://'.format(optbase))
    os.chdir(d)
    print(os.getcwd())


def favdir():
    with open("D://codes//Windows//often.txt", 'r') as e:  # Your file with locations
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
        if os.path.isdir(i):
            dis = ('{} - {}'.format(a, i))
            print(colored(dis, 'red'))
            del dis
        elif os.path.isfile(i):
            dis = ('{} - {}'.format(a, i))
            print(colored(dis, 'green'))
            del dis
        a = a + 1
        dirlist.append(i)
    space()
    print(colored('1 - {}'.format(int(a) - 1), 'yellow'), " - select file/dir")
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
        favdir()
        optfav = input(" Choose a directory ")
        os.chdir(favdir()[int(int(optfav) - 1)])
        print(os.getcwd())
        del opt
    elif opt == "view":
        print("Under Construction")
        #       v = int(viewno) - 1
        #       print(os.stat(dirlist[int(v)]))
        del opt
    elif opt == "prev":
        os.chdir('..')
        del opt
    else:
        if os.path.isfile(dirlist[int(int(opt) - 1)]):
            os.startfile(dirlist[int(int(opt) - 1)])
            del opt
        elif os.path.isdir(dirlist[int(int(opt) - 1)]):
            os.chdir(dirlist[int(int(opt) - 1)])
            os.listdir(os.getcwd())
            del opt
