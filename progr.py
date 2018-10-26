import os
string="python is scripting language"
list_files=[]
for f in os.listdir("/home/siddasah/data"):
        if f.endswith(".txt"):
            data=open(f,'r')
            req_data=data.read()
            if string in req_data:
                print "filename is: ",f
