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
	# md, some file look like "-2-22 1487931 7204102343231"
	# but some file look like "-2-" and another line, wtf
	# so it depends you, you should use foxit reader to open the pdf file
    if input_line.startswith('-'):   
        list = input_line.split(' ')
        pos = list[0].index('-', 1, -1)
        id = list[0][pos+1:]
        line = id + ' ' + list[1] + ' ' +list[2]
    else:
        line = input_line
    print line
    output_file.write(line)
    input_line = input_file.readline()

input_file.close()
output_file.close()