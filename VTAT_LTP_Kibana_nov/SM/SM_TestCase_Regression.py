#!/usr/bin/python
import requests
import time

#Support files
def test_idf_with_correct_path_support():
	r = requests.get("http://192.168.4.19:8866/IDF_Store/idf_store.html?path=/home/yerikgan/TEST/supported/",
					 headers={'Content-Type': 'application/json'})
	with open("test_idf_with_correct_path_support.log", "w+") as log_file:
		time.ctime()
		log_file.write("*"*45+"\n")	
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) != 200


def test_idf_with_incorrect_path_support():
	r = requests.get("http://192.168.4.19:8866/IDF_Store/idf_store.html?path=/home/yerikgan/TEST2/supported/",
					 headers={'Content-Type': 'application/json'})
	with open("test_idf_with_incorrect_path_support.log", "w+") as log_file:
		time.ctime()
		log_file.write("*"*45+"\n")
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) != 200


def test_idf_with_correct_path_files_support(file_type):
	r = requests.get("http://192.168.4.19:8866/IDF_Store/idf_store.html?path=/home/yerikgan/TEST/supported/"+file_type,
					 headers={'Content-Type': 'application/json'})
	with open("test_idf_with_correct_path_files_support.log", "w+") as log_file:
		time.ctime()
		log_file.write("*"*45+"\n")	
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) == 200


def test_idf_with_incorrect_path_files_support(file_types):
	r = requests.get("http://192.168.4.19:8866/IDF_Store/idf_store.html?path=/home/yerikgan/TEST3/supported/"+file_types,
					 headers={'Content-Type': 'application/json'})
	with open("test_idf_with_incorrect_path_files_support.log", "w+") as log_file:
		time.ctime()
		log_file.write("*"*45+"\n")
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) == 200


def test_idf_file_search_exist_support(file_type):
	r = requests.get("http://192.168.4.19:8876/IDF_Retrieve/idf_file_search?q="+file_type,
					 headers={'Content-Type': 'application/json'})
	with open("test_idf_file_search_exist_support.log", "w+") as log_file:
		time.ctime()
		log_file.write("*"*45+"\n")
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) == 200


def test_idf_file_search_not_exist_support():
	r = requests.get("http://192.168.4.19:8876/IDF_Retrieve/idf_file_search?q=StarFish.jpg",
					 headers={'Content-Type': 'application/json'})
	with open("test_idf_file_search_not_exist_support.log", "w+") as log_file:
		time.ctime()
		log_file.write("*"*45+"\n")
		log_file.write(time.strftime('%l:%M%p on %b %d, %Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n')
	return int(r.content[15:18]) != 200


def test_idf_content_search_exist():
	r = requests.get("http://192.168.4.19:8876/IDF_Retrieve/idf_content_search?q=Votary",
						headers={'Content-Type': 'application/json'})
	with open("test_idf_content_search_exist.log", "w+") as log_file:
		log_file.write("*"*45+"\n")
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) == 200


def test_idf_content_search_not_exist():
	r = requests.get("http://192.168.4.19:8876/IDF_Retrieve/idf_content_search?q=Qualcomm",
						headers={'Content-Type': 'application/json'})
	with open("test_idf_content_search_not_exist.log", "w+") as log_file:
		log_file.write("*"*45+"\n")
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) != 200


def test_idf_manage_by_valid_date():
	r = requests.get("http://192.168.4.19:8856/IDF_Manage/idf_file_search_manage?from_date=2009-02-28&to_date=2017-04-01",
						headers={'Content-Type':'application/json'})
	with open("test_idf_manage_by_valid_date.log", "w+") as log_file:
		log_file.write("*"*45+"\n")			
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) == 200


def test_idf_manage_by_invalid_date():
	r = requests.get("http://192.168.4.19:8856/IDF_Manage/idf_file_search_manage?from_date=2017-06-30&to_date=2017-07-20",
						headers={'Content-Type':'application/json'})
	with open("test_idf_manage_by_invalid_date.log", "w+") as log_file:
		log_file.write("*"*45+"\n")	
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) != 200

#UnSupport files
def test_idf_with_correct_path_unsupport():
	r = requests.get("http://192.168.4.19:8866/IDF_Store/idf_store.html?path=/home/yerikgan/TEST/unsupported/",
					 headers={'Content-Type': 'application/json'})
	with open("test_idf_with_correct_path_unsupport.log", "w+") as log_file:
		time.ctime()
		log_file.write("*"*45+"\n")
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) != 200


def test_idf_with_incorrect_path_unsupport():
	r = requests.get("http://192.168.4.19:8866/IDF_Store/idf_store.html?path=/home/yerikgan/TEST2/unsupported/",
					 headers={'Content-Type': 'application/json'})
	with open("test_idf_with_incorrect_path_unsupport.log", "w+") as log_file:
		time.ctime()
		log_file.write("*"*45+"\n")
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) != 200

def test_idf_with_correct_path_files_unsupport(file_types):
	r = requests.get("http://192.168.4.19:8866/IDF_Store/idf_store.html?path=/home/yerikgan/TEST/unsupported/"+file_types,
					 headers={'Content-Type': 'application/json'})
	with open("test_idf_with_correct_path_files_unsupport.log", "w+") as log_file:
		time.ctime()
		log_file.write("*"*45+"\n")
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) == 200


def test_idf_with_incorrect_path_files_unsupport(file_types):
	r = requests.get("http://192.168.4.19:8866/IDF_Store/idf_store.html?path=/home/yerikgan/TEST3/unsupported/"+file_types,
					 headers={'Content-Type': 'application/json'})
	with open("test_idf_with_incorrect_path_files_unsupport.log", "w+") as log_file:
		time.ctime()
		log_file.write("*"*45+"\n")
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) == 200


def test_idf_file_search_exist_unsupport(file_types):
	r = requests.get("http://192.168.4.19:8876/IDF_Retrieve/idf_file_search?q="+file_types,
					 headers={'Content-Type': 'application/json'})
	with open("test_idf_file_search_exist_unsupport.log", "w+") as log_file:
		time.ctime()
		log_file.write("*"*45+"\n")
		log_file.write(time.strftime('%I:%M:%S%p on %d-%B-%Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n'*2)
	return int(r.content[15:18]) == 200


def test_idf_file_search_not_exist_unsupport():
	r = requests.get("http://192.168.4.19:8876/IDF_Retrieve/idf_file_search?q=Fish.png",
					 headers={'Content-Type': 'application/json'})
	with open("test_idf_file_search_not_exist_unsupport_.log", "w+") as log_file:
		time.ctime()
		log_file.write("*"*45+"\n")
		log_file.write(time.strftime('%l:%M%p on %b %d, %Y')+'\n'*2)
		log_file.write("Status Code = "+str(r.status_code)+'\n'*2)
		log_file.write("Content = "+r.content+'\n')
	return int(r.content[15:18]) != 200


