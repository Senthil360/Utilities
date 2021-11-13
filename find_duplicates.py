import os
import sys
import glob
import argparse
from typing import Optional

parser = argparse.ArgumentParser()
parser.add_argument('Source_Directory', type=str,
                    help="Specify your Source Directory")
parser.add_argument('Destination_Directory', type=str,
                    help="Specify the Destination Directory")
parser.add_argument('File_Extension', type=str,
                    help="File extension to search")
parser.add_argument('Not_Recursive', nargs='?', type=int, const=0)

args = parser.parse_args()

source_directory = args.Source_Directory+'\\'
destination_directory = args.Destination_Directory+'\\'
extension = args.File_Extension
not_recursive = args.Not_Recursive


def fileSize(file):
    return(os.stat(file).st_size)


def getDuplicates():

    duplicates = 0

    for source_files in os.listdir(source_directory):
        for dest_files in os.listdir(destination_directory):
            if fileSize(os.path.join(source_directory, source_files)) == fileSize(os.path.join(destination_directory, dest_files)
            ) and os.path.isfile(source_directory+source_files) and os.path.abspath(dest_files
            ) != os.path.abspath(source_files):
                duplicates += 1
                print(os.path.join(source_directory, source_files) ,
                      os.path.join(destination_directory, dest_files))

    print(duplicates, " duplicates found")


def recursiveCheck():

    duplicates = 0

    source_list = glob.glob('{source_directory}/**/*.{ext}'.format(
        source_directory=source_directory, ext=extension), recursive=True)
    destination_list = glob.glob('{dest_directory}/**/*.{ext}'.format(
        dest_directory=destination_directory, ext=extension), recursive=True)

    for source_files in source_list:
        for dest_files in destination_list:
            if fileSize(source_files) == fileSize(dest_files) and os.path.abspath(dest_files) != os.path.abspath(source_files):
                duplicates += 1
                print(source_files, dest_files)

    print(duplicates, " duplicates found")


# recursiveCheck()

if __name__ == '__main__':
    if not_recursive != 0:
        getDuplicates()
    else:
        recursiveCheck()
