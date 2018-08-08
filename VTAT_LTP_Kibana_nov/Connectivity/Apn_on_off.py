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



def APN_On_Off():
	global adb_dev
	#Number of Iteration
	Iterations=100
	for i in range(Iterations):
		for Apn_dev in adb_dev:
			enab1="adb -s "+Apn_dev+" shell settings put global airplane_mode_on 1"
			#adb -s HQ541YL17255 shell settings put global airplane_mode_on 1
			exe=os.system(enab1)
			enab2="adb -s "+Apn_dev+" shell am broadcast -a android.intent.action.AIRPLANE_MODE" 		
			exeE=os.system(enab2)

			if exeE==0:
				print "\nAPN turn on successfully in ",Apn_dev," device"
			else:
				pass
			time.sleep(3)
		for Apn_dev in adb_dev:
			enab3="adb -s "+Apn_dev+" shell settings put global airplane_mode_on 0"
			exe=os.system(enab3)
			enab4="adb -s "+Apn_dev+" shell am broadcast -a android.intent.action.AIRPLANE_MODE" 		
			exeD=os.system(enab4)
			if exeD==0:
				print "\nAPN turn off successfully in ",Apn_dev," device"
			else:
				pass
			time.sleep(3)


dev_id_and_ip()
APN_On_Off()

'''
#commands:

#Enable:
adb shell settings put global airplane_mode_on 1
adb shell am broadcast -a android.intent.action.AIRPLANE_MODE

#Disable:
adb shell settings put global airplane_mode_on 0
adb shell am broadcast -a android.intent.action.AIRPLANE_MODE
'''
