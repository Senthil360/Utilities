import os
import sys

for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
        pass

def renamer(orig, mod):
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file) and file.endswith(orig):
            print(file[0:file.rfind('.')]+mod)
            os.rename(file, file[0:file.rfind('.')]+'.'+mod)
        else :
            print("No {ext} file found".format(ext=orig))


if __name__ == "__main__":
    renamer(sys.argv[1], sys.argv[2])