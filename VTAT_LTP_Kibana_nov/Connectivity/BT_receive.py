# this is a program for File transform from a device to PC
# In order to run this first your devicesn has to be paired with one another
import os,time,subprocess,threading
class filetransfer():
	def __init__(self):
		#self.cmd = cmd
		self.process = None
		print "=================Welcome to transfer world======================"

	def send(self,mac_address):
		#path = "/home/thangsai/Desktop/Bluetooth/blu.py"
	        path = input("Enter the path of the files")
		cmd = "bt-obex -p {} {}".format(mac_address,path)
		os.system(cmd)
 		#print "=========Files has been sucessfully transfered============="

	def receive(self, timeout):
        	def target():
        		cmd = "bt-obex -s"
            		self.process = subprocess.Popen(cmd, shell=True)
            		self.process.communicate()
            

        	thread = threading.Thread(target=target)
        	thread.start()
        	thread.join(timeout)
        	self.process.terminate()
        	thread.join()

if __name__ == "__main__":
	
	f = filetransfer()
	print "please press the accept pop-up in your device"
	#f.send("BC:F5:AC:02:96:23")
	#f.send(mac_address)
	#time.sleep(3)
	print "=========Files has been sucessfully trasfered by the system============="
	print "==========system server is waiting for the files to receive========="
	f.receive(timeout=30)
	print "=========Files has been sucessfully received by the system============="
	

os.system("killall 'bt-obex'")
print "Your time has been completed"

	
	

