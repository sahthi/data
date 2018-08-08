#!/usr/bin/python
import MySQLdb,time
def mysql_Truncate_Table(Table):
	db = MySQLdb.connect(host="localhost",    	# your host, usually localhost
		user="Test_Team",         		# your username
                passwd="votary",  			# your password
                db="DM_Testing")                        # name of the data base
	# you must create a Cursor object. It will let
	#  you execute all the queries you need
	cur = db.cursor()
	if "DM_Discover"== Table:
		cur.execute("truncate DM_Discover")
	elif "DM_GET"== Table:
		cur.execute("truncate DM_GET")
	elif "DM_Observe"==Table:
		cur.execute("truncate DM_Observe")
	db.commit()
#	time.sleep(3)

def mysql_Fetch_Discover():
	Discover_List=[]
	db = MySQLdb.connect(host="localhost",    
		user="Test_Team",                 
                passwd="votary",                 
                db="DM_Testing")                 
	cur = db.cursor()
	cur.execute("select * from DM_Discover")
	for row in cur.fetchall():
		print "****************************************"
	        print"Resource_Name :",row[1]
                print"Resource_Handle :",row[2]
                print "****************************************"
	        Discover_List.append(row[2])
	return Discover_List

def mysql_Fetch_Updated_Discover():
	Discover_List=[]
	db = MySQLdb.connect(host="localhost",    
		user="Test_Team",                 
                passwd="votary",                 
                db="DM_Testing")                 
	cur = db.cursor()
	cur.execute("select * from DM_Discover")
	for row in cur.fetchall():
		Discover_List.append(row[2])
	return Discover_List

def mysql_Fetch_Handle(Table,inputHandle):
        key_val = 0
	Discover_List=[]
	db = MySQLdb.connect(host="localhost",     # your host, usually localhost
                     user="Test_Team",             # your username
                     passwd="votary",              # your password
                     db="DM_Testing")              # name of the data base
	print "\nInformation of Device handle : ",inputHandle
	cur = db.cursor()
	if "DM_GET"==Table:
		cur.execute("select * from DM_GET where Handle='{}'".format(inputHandle))
		for row in cur.fetchall():
		    print "****************************************"
		    print "ID** ",row[0], " " ," Resource : ",row[1], " Handle :",row[2] , " key : ",row[3] ," value :" ,row[4]
		    print "****************************************"    
		    if(row[3] == 'power'):
			#	print "row[4] :", type(row[4])
				key_val =  row[4]
		return key_val

	elif "DM_Observe"==Table:
		cur.execute("select * from DM_Observe where Handle='{}'".format(inputHandle))
		for row in cur.fetchall():
		    print "Handle :",row[2] , "key : ",row[3] ,"value :" ,row[4]

def mysql_fetech_value(inputHandle):
	db = MySQLdb.connect(host="localhost",     
        	user="Test_Team",                  
                passwd="votary",                   
                db="DM_Testing")                   
	cur = db.cursor()
	cur.execute("select count(ID) from DM_GET where Handle='{}'".format(inputHandle))
	for row in cur.fetchall():	
		
		if row[0]==0:         # if no row found[put before get]  
			#print "Handle not found"
			return 0
		else:
			cur.execute("select value from DM_GET where Handle='{}' and key1='{}'".format(inputHandle,"power"))
			for row in cur.fetchall():
				return int(row[0])
	

def mysql_Delete_Handle(Table,inputHandle):
	db = MySQLdb.connect(host="localhost",    
        	user="Test_Team",                 
                passwd="votary",                  
                db="DM_Testing")                  

	cur = db.cursor()
	if "DM_GET"==Table:
		cur.execute("delete from DM_GET where Handle='{}'".format(inputHandle))
	elif "DM_Observe"==Table:
		cur.execute("delete from DM_Observe where Handle='{}'".format(inputHandle))
	db.commit()
