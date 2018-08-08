#BT_on_off
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



def BT_On_Off():
	global adb_dev
	#Number of Iteration
	Iterations=100
	for i in range(Iterations):
		for bt_dev in adb_dev:
			enab="adb -s "+bt_dev+" shell service call bluetooth_manager 6 for BT-enabling"	
			exe=os.system(enab)
			if exe==0:
				print "\nBT turn on successfully in ",bt_dev," device"
			else:
				pass
			time.sleep(3)
		for bt_dev in adb_dev:
			disb="adb -s "+bt_dev+" shell service call bluetooth_manager 8 for BT-Disabling"	
			exe=os.system(disb)
			if exe==0:
				print "\nBT turn off successfully in ",bt_dev," device"
			else:
				pass
			time.sleep(3)


dev_id_and_ip()
BT_On_Off()

#Commands :
#adb shell service call bluetooth_manager 6 for BT-enabling
#adb shell service call bluetooth_manager 8 for BT-Disabling


