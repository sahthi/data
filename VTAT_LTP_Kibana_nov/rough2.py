import subprocess,os
cmd = "python run.py discover 1 >dm_test.log"
"""try:
	p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out,err = p.communicate()
	print (out,err)
except Exception:
	print("error")"""

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print BASE_DIR

print os.getcwd()

os.chdir("/opt/ltp")
print os.getcwd()

print BASE_DIR
