#!/usr/bin/python
from sys import argv
from SM_TestCase_Automate import *

options = ['correct_path', 'incorrect_path', 'content_exist', 
			'content_not_exist', 'file_exist', 'file_not_exist',
			'date_exist', 'date_not_exist']

functions = [test_idf_with_correct_path, test_idf_with_incorrect_path,
				test_idf_content_search_exist, test_idf_content_search_not_exist,
				test_idf_file_search_exist, test_idf_file_search_not_exist,
				test_idf_manage_by_valid_date, test_idf_manage_by_invalid_date]

arguments = dict(zip(options, functions))

# print arguments

if len(argv) > 1:
	if len(argv)==3:
		for val in range(int(argv[2])):
			arguments[argv[1]]()
	else:
		arguments[argv[1]]()
