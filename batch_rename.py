import os
import sys
import argparse

"""
Senthil360 @XDA-Developers.com
<senthilmanikandan360@gmail.com>
Batch rename a single file format to another
"""

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input-form', help='Your input file format', required=True)
parser.add_argument('-o', '--output_form', help='Your output file format', required=True)
args = parser.parse_args()


def rename_ext_only():
    fol = (os.path.dirname(
        os.path.abspath(sys.argv[0])))  # Sticking to sys.argv[0] as argparse does not have that specific API yet;
    ab = [a for a in (os.listdir(fol)) if a.endswith(args.input_form)]
    print("Number of", args.input_form, "files = ", len(ab))
    c = 0
    for b in ab:
        try:
            input = b
            output = str(c) + args.output_form
            os.rename(input, output)
            c = c + 1
        except FileNotFoundError:
            print("Error")

    print("Converted all", len(ab), args.input_form, "to", args.output_form)


rename_ext_only()
