## g is input directory
import filecmp
import os
from os import walk


# Create mod and base directories for comparisons and place your files or folders there

def compareDirs(g):
    mydir = list()
    for root, dirs, files in os.walk(g):
        if dirs:
            mydir.append(os.path.splitext(root)[0])
    moddir_one = set(mydir)
    moddir = list(moddir_one)
    return moddir


def checkFolderEquality(dir1, dir2):
    dirs_cmp = filecmp.dircmp(dir1, dir2)
    if len(dirs_cmp.left_only) > 0:
        print("Base directory EXTRA files", dirs_cmp.left_only)
        print()
    (_, mismatch, errors) = filecmp.cmpfiles(dir1, dir2, dirs_cmp.common_files, shallow=False)
    if len(mismatch) > 0:
        print(dir1)
        print(mismatch)
        return False


modfinal = (compareDirs("mod"))
basefinal = [w.replace('mod', 'base') for w in modfinal]

dirlength = (len(modfinal))
initial_length = 0
while (initial_length < dirlength):
    base_dir = (basefinal[initial_length])
    mod_dir = (modfinal[initial_length])
    checkFolderEquality(base_dir, mod_dir)
    initial_length = initial_length + 1
    del base_dir
    del mod_dir
