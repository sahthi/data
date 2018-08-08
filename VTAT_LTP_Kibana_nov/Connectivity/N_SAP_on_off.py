import os,time
#Getting adb devices
cmd = "adb devices"
os.system(cmd)

#Select the device
wifi_dev=raw_input("Enter the device details : ")
#Number of Iteration
Iterations=input("Enter the number of iterations you want : ")
#SAP_Enable
for i in range(Iterations):
	if i==0:
		os.system("adb shell input keyevent 3")
		os.system("adb shell am start -n com.android.settings/.TetherSettings")
		os.system("adb shell input keyevent 20 66")
		os.system("adb shell input keyevent 61 61 66")
		time.sleep(5)
	#SAP_Disable
		os.system("adb shell input keyevent 3")
		os.system("adb shell am start -n com.android.settings/.TetherSettings")
		os.system("adb shell input keyevent 66 66")
		os.system("adb shell input keyevent 61 61 66")
		time.sleep(5)
	else:
		os.system("adb shell input keyevent 3")
		os.system("adb shell am start -n com.android.settings/.TetherSettings")
		os.system("adb shell input keyevent 66")
		os.system("adb shell input keyevent 61 61 66")
		time.sleep(5)
	#SAP_Disable	
		os.system("adb shell input keyevent 3")
		os.system("adb shell am start -n com.android.settings/.TetherSettings")
		os.system("adb shell input keyevent 66 66")
		os.system("adb shell input keyevent 61 61 66")
		time.sleep(5)

