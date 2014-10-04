#@uncle nought
# -*- coding:utf-8 -*-

import csv
import os
import sqlite3
import math
import sys

input_filename = sys.argv[1]
output_filename = 'mysql_'+ input_filename
input_file = open(input_filename)
output_file = open(output_filename, 'w')
input_line = input_file.readline()
while input_line:
    line = ''
    if input_line.startswith('-'):
        list = input_line.split(' ')
        pos = list[0].index('-', 1, -1)
        id = list[0][pos+1:]
        line = id + ' ' + list[1] + ' ' + list[2] + ' ' + list[3]
    else:
        line = input_line
    
    input_line = input_file.readline()
    if input_line[0:1] >= '1' and input_line[0:1] <= '9':
        print line
        output_file.write(line)
        continue;
    elif input_line[0:1] == '-':
        print line
        output_file.write(line)
        continue;
    else:
        line = line[0:-1] + input_line;
        print line
        output_file.write(line)
        input_line = input_file.readline()

input_file.close()
output_file.close()