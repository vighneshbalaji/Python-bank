import sqlite3

conn = sqlite3.connect('student.db')

def insvall(did,dname,dage) :
	
	conn.execute("INSERT INTO cls12 (id,name,age) VALUES(?, ?, ?)", (did,dname,dage) )



	conn.commit()

	cursor = conn.execute("SELECT * FROM cls12")
	y = '-' * 27
	print("Id    Name              AGE")
	print(y)
	for row in cursor:
	   print ("%2d %-20s %2d"% (row[0],row[1],row[2] )  ) # old method fine
	  #int ("{0} {1} {2}".format(str(row[0]),row[1],str(row[2]) )  )  # Works Fine
	print(y)
	print()
	print ("Operation done successfully")


def delvall(did) :
		

	# Works Fine
	conn.execute("DELETE FROM cls12 WHERE id = ?" ,(did,)  )
	conn.commit()

	#print ("Records deleted successfully")

	cursor = conn.execute("SELECT * FROM cls12")
	y = '-' * 27
	print("Id    Name              AGE")
	print(y)
	for row in cursor:
	   print ("%2d %-20s %2d"% (row[0],row[1],row[2] )  ) # old method fine
	  #int ("{0} {1} {2}".format(str(row[0]),row[1],str(row[2]) )  )  # Works Fine
	print(y)
	print()
	print ("Operation done successfully")


def chckupdt(did) :

	cursor = conn.execute("SELECT name FROM cls12 WHERE id = ?",(did,))
	
	result = cursor.fetchall()
	rowcount = len(result)
	
	if(rowcount == 1):
		for row in result:
			dname = row[0]
	else:
		return("")
	
	return(dname)


def updt(did,dname):

	conn.execute("UPDATE cls12 SET name= ?  WHERE ID = ?", (dname,did) )
	conn.commit()
	
	cursor = conn.execute("SELECT * FROM cls12")
	y = '-' * 27
	print("Id    Name              AGE")
	print(y)
	for row in cursor:
	   print ("%2d %-20s %2d"% (row[0],row[1],row[2] )  ) # old method fine
	  #int ("{0} {1} {2}".format(str(row[0]),row[1],str(row[2]) )  )  # Works Fine
	print(y)
	print()
	print ("Operation done successfully")
	val = input("Press any key to continue... ")

def conclose():
	conn.close()
	print "Connection is closed"
	
