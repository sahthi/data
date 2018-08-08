import re,os,subprocess,time
from subprocess import call,Popen,PIPE

def dev_id_and_ip():
#Getting adb devices
	global SAP_ID
	global SAP_IP
	global GO_ID
	global GO_IP
	global adb_dev
	global dev_ip
	adb_dev=[]
	dev_ip={}	
	cmd = "adb devices"
	os.system(cmd)
	adb_output = Popen(cmd, shell = True,stderr = PIPE,stdout = PIPE)
	out,err = adb_output.communicate()
	data = re.findall( r'([a-zA-Z]+[0-9]+[a-zA-Z0-9]+)|([0-9]+[a-zA-Z]+[0-9a-zA-Z]+)',out,re.M )
	for i in data:
		for j in i:
			if j:
				adb_dev.append(j)

	#print adb_dev,"\n"

def wifi_scanning():
	global adb_dev
	#Number of Iteration
	for wifi_dev in adb_dev:
		cmd="adb -s "+wifi_dev+" shell "+"dumpsys wifi"
		adb_output = Popen(cmd, shell = True,stderr = PIPE,stdout = PIPE)
		out,err = adb_output.communicate()
		data=out
	#print data,type(data)
		data=data.split("\n")
		lis=[]
		AP=[]
		word="[ESS]"
		for i in data:
			if word in i :
				lis.append(i)
		print "\nScanning is done","\n","list of available AP's : \n"
		for j in lis:
			j=j.split("[ESS]")[1]
			AP.append(j)
		print wifi_dev,AP
		

dev_id_and_ip()
wifi_scanning()
	
