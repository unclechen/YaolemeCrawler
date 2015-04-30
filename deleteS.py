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
    if input_line == '\n' :
        input_line = input_file.readline()
        continue
    else:
        line = input_line
    print line
    output_file.write(line)
    input_line = input_file.readline()

input_file.close()
output_file.close()
