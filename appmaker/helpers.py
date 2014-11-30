__author__ = 'Beka'
import fileinput
import string
import sys
import errno


def make_file(dir_name,file_name):
    temp_path = dir_name +'\\'+ file_name
    file = open(temp_path, 'w')
    file.close()
