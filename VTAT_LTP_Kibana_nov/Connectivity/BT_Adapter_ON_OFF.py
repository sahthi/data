import os,time
# first type sudo -i and give the password
cmd2 =  "bluetooth off"
os.system(cmd2)
time.sleep(10)
cmd3 = "bluetooth on"
os.system(cmd3)
