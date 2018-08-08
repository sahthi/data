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
def Wifi_On_Off():
	global adb_dev
	#Number of Iteration
	Iterations=5
	for i in range(Iterations):
		for wifi_dev in adb_dev:
			enab="adb -s "+wifi_dev+" shell "+"svc wifi enable"
			exe=os.system(enab)
			if exe==0:
				print "\nWifi turn on successfully in ",wifi_dev," device"
			else:
				pass
			time.sleep(3)
		for wifi_dev in adb_dev:
			disb="adb -s "+wifi_dev+" shell "+"svc wifi disable"
			exe=os.system(disb)
			if exe==0:
				print "\nWifi turn off successfully in ",wifi_dev," device"
			else:
				pass
			time.sleep(3)

dev_id_and_ip()
Wifi_On_Off()
