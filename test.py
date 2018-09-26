import os,subprocess
base = os.getcwd()
base_file = os.path.join(base,"avd/")
for test in os.listdir(base_file):
	os.chdir(base_file)
	if test.endswith(".py"):
		process = subprocess.Popen('python {0}'.format(test), shell=True)
		status = process.communicate()

