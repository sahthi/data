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

def LCD_On_Off():
	global adb_dev
	#Number of Iteration
	Iterations=5
	for i in range(Iterations):
		for lcd_dev in adb_dev:
			enab="adb -s "+lcd_dev+" shell input keyevent 26"
			exe=os.system(enab)
			if exe==0:
				print "\nLCD turn on successfully in ",lcd_dev," device"
			else:
				pass
			time.sleep(3)
		for lcd_dev in adb_dev:
			disb="adb -s "+lcd_dev+" shell input keyevent 26"
			exe=os.system(disb)
			if exe==0:
				print "\nLCD turn off successfully in ",lcd_dev," device"
			else:
				pass
			time.sleep(3)

dev_id_and_ip()
LCD_On_Off()


'''
#Commands:
adb shell input keyevent KEYCODE_POWER

or

adb shell input keyevent 26
'''
