import re
import sys
import argparse
from os import path

p = argparse.ArgumentParser(description='Parse detected objects in image.')
p.add_argument(
    '-f','--file',dest='f_in',action='store',default='./sample_in.txt',
    help='input file'
)
p.add_argument(
    '-o','--output',dest='f_out',action='store',default='./sample_out.txt',
    help='output file'
)
p.add_argument(
    '-a','--append',dest='append',action='store_true',
    help='append to output file'
)
args = p.parse_args()

f = open(args.f_in, "r")
lines = f.readlines()
f.close()

new_lines = ""
pattern = re.compile(".*%$")
for line in lines:
		if re.search(pattern, line):
				new_lines += line

if args.append and path.exists(args.f_out):
		f = open(args.f_out, "a+")
		f.write("\n"+new_lines)
else:
		f = open(args.f_out, "w")
		f.write(new_lines)
f.close()
