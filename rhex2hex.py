import sys;
from os import path;
import re;

def add_spaces(string, length):
  return ' '.join(string[i:i+length] for i in range(0,len(string),length))

if len(sys.argv) != 3:
  print("Usage: rhex2hex [infile] [outfile]\n");
  exit();

if not path.isfile(sys.argv[1]):
  print("[!] " + sys.argv[1] + " not found.\n");
  exit();

with open(sys.argv[1]) as infile:
  content = infile.readlines();
  content = [x.strip() for x in content]

regex  = re.compile('[^a-zA-Z0-9]')
offset = 0;
prefix_maxlen = 10;



outfile = open(sys.argv[2], 'w+');


for line in content:
  line = regex.sub('', line);
  hex_count = len(line)/2
  # Zero prefix offset 
  prefix = '0'*(prefix_maxlen - len(str(hex(offset))[2:]))
  # [2:] => Remove '0x' prefix 
  print_offset = str(prefix) + str(hex(offset))[2:];
  hexval = add_spaces(line,2);
  outfile.write(print_offset + " " + hexval + "\n");
  print(print_offset + " " + hexval + "\n"); 
  offset = offset + hex_count;


outfile.close();




