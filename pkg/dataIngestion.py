import mysql.connector
import MySQLdb


class createDBConnection():
	"""
	Create a personal user in MySQL
	---------------------------------
	First, log in as root
	Then, create the cursor to iterate over rows returned by a query
	Then, create the user
	"""
	pass

#try:
#	mydb = mysql.connector.connect(
#	  host="localhost",
#	  user="root",
#	  passwd="root"
#	)
#
#	mkuser = 'alex'
#	host = 'localhost'
#
#	creation = "CREATE USER '%s'@'%s'" %(mkuser, host)
#	results = cursor.execute(creation)
#
#	print(results)
#
#	#mydb = MySQLdb.connect(host = 'localhost', 
#	#                       user = 'root', 
#	#                       passwd = 'rootsecret')
##
#	#cursor = mydb.cursor()
##
#	#statement = """CREATE USER 'alex'@'localhost' IDENTIFIED BY 'alex'""" 
##
#	#cursor.execute(statement)
#
#except Exception as e:
#	print(e)#