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

	
	for i in adb_dev:
		cmd= "adb -s "+i+" shell netcfg | grep wlan0"
	#Getting ip addresses
		adb_ip = Popen(cmd, shell = True,stderr = PIPE,stdout = PIPE)
		out_ip,err_ip = adb_ip.communicate()
		ip_data= re.findall( r'[0-9]+(?:\.[0-9]+){3}', out_ip)
		for j in ip_data:
			ip=j	
			dev_ip[i]=ip
	print "\nDevices and IP addresses : ",dev_ip
	#SAP and GO details	
	for i in dev_ip.keys():
		if dev_ip[i] == "192.168.43.1":
			SAP_ID=i
			SAP_IP="192.168.43.1"
		elif dev_ip[i] == "192.168.49.1" :
			GO_ID=i
			GO_IP="192.168.49.1"
		else:
			pass
		
	#Getting ip address of PC
	global sys_ip
	cmd = "hostname -I"
	adb_output = Popen(cmd, shell = True,stderr = PIPE,stdout = PIPE)
	out,err = adb_output.communicate()
	sys_ip = out.strip()
	print sys_ip


def P2P_UDP_UL():
	global SAP_ID
	global SAP_IP
	global GO_ID
	global GO_IP
	global adb_dev
	global dev_ip
	global sys_ip
	for dev in adb_dev:
		if dev != GO_ID :
			STA_ID=dev
			STA_IP=dev_ip[dev]
			Band_width="30M"
			Time_limit="300" #seconds
		
			UL_server_cmd=" gnome-terminal -e 'adb -s "+GO_ID+" shell iperf -s -u -i 1' "
			UL_client_cmd=" gnome-terminal -e 'adb -s "+STA_ID+" shell iperf -c "+GO_IP+" -u -b "+Band_width+" -i 1 -t "+Time_limit+" '"
			os.system(UL_server_cmd)
			os.system(UL_client_cmd)
			time.sleep(2)
		else:
			pass

dev_id_and_ip()
P2P_UDP_UL()

