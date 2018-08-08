#!/usr/bin/python
from SM_TestCase_Regression import *
import sys
#list_arg = sys.argv
list_arg = sys.argv[1:]
options_s =['correct_path_support', 
				'incorrect_path_support',			
				'correct_path_files_support',
				'incorrect_path_files_support',
				'file_search_exist_support',
				'file_search_not_exist_support',
				'content_exist',
				'content_not_exist',
				'date_exist', 	
				'date_not_exist']

functions_s =[test_idf_with_correct_path_support,
				test_idf_with_incorrect_path_support,			
				test_idf_with_correct_path_files_support,
				test_idf_with_incorrect_path_files_support,
				test_idf_file_search_exist_support, 											    					  
				test_idf_file_search_not_exist_support,
				test_idf_content_search_exist,
				test_idf_content_search_not_exist,
				test_idf_manage_by_valid_date,
				test_idf_manage_by_invalid_date]

options_un =['correct_path_unsupport',
				'incorrect_path_unsupport',
				'correct_path_files_unsupport',
				'incorrect_path_files_unsupport',
				'file_search_exist_unsupport',
				'file_search_not_exist_unsupport']

functions_un =[test_idf_with_correct_path_unsupport,
				 test_idf_with_incorrect_path_unsupport,
				 test_idf_with_correct_path_files_unsupport,
				 test_idf_with_incorrect_path_files_unsupport,	
				 test_idf_file_search_exist_unsupport,
				 test_idf_file_search_not_exist_unsupport]

file_types_s = ["Jellyfish.jpg", "sample.mp4","AppBody-Sample-English.docx","DAR_Mounika.ods", "example.odg", "hello.doc", "java.pdf","jsvsnodejs.odt","nls.xls","Thumbs.db","VITA_EnggL1_ApprovedDraft.odp","VITA -SM -Model.xlsx"]

file_types_us = ["daily.bat","gpslistener.zip","hello.py","java-json.jar","Kalimba.mp3","new.html","Sample.txt", "sel.png", "UTServices.java","web.xml"]
s_arguments = dict(zip(options_s, functions_s))
un_arguments = dict(zip(options_un, functions_un))

if len(list_arg) % 2 == 0 and len(list_arg) != 0 :
	for index in range(0,len(list_arg),2):
		if list_arg[index] in s_arguments.keys():
			if ((list_arg[index] == 'correct_path_files_support' or list_arg[index] == 'file_search_exist_support')or
				(list_arg[index] == 'incorrect_path_files_support')):
				for val in range(int(list_arg[index + 1])):
					for value in file_types_s:
						s_arguments[list_arg[index]](value)
				print list_arg[index],"Testcase ran",list_arg[index + 1],"time/s"
			else:
				for val in range(int(list_arg[index + 1])):
					#for value in file_types_s:
					s_arguments[list_arg[index]]()
				print list_arg[index],"Testcase ran",list_arg[index + 1],"time/s"
		else:	
	
			if ((list_arg[index] == 'correct_path_files_unsupport' or list_arg[index] == 'file_search_exist_unsupport')or
				(list_arg[index] == 'incorrect_path_files_unsupport')):
				for val in range(int(list_arg[index + 1])):
					for value in file_types_us:
						un_arguments[list_arg[index]](value)
				print list_arg[index],"Testcase ran",list_arg[index+1],"time/s"
			else:
				for val in range(int(list_arg[index+1])):
					#for value in file_types_us:
					un_arguments[list_arg[index]]()	
				print list_arg[index],"Testcase ran",list_arg[index + 1],"time/s"
				  
else:
	print "Module or no. Iterations Error"			
