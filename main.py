import mysql.connector
import MySQLdb
import sys
#inhouse

class dataBase(object):
	"""
	Create a personal user in MySQL
	---------------------------------	
	First, log in as root
	Then, create the cursor to iterate over rows returned by a query
	Then, create the user
	"""
	def __init__(self, hostValue, userValue, passwdValue, newUser=None, newHost=None, newPass=None):
		self.hostValue = hostValue
		self.userValue = userValue
		self.passwdValue = passwdValue
		self.newUser = newUser
		self.newHost = newHost
		self.newPass = newPass

	def createConnection(self):
		try:
			mydb = mysql.connector.connect(
			  host=self.hostValue,
			  user=self.userValue,
			  passwd=self.passwdValue
			)
			return mydb
		except Exception as e:
			print (e)
			return 1

	def createUser(self, cursor, newHost, newUser, newPass):
		try:
			#print (newHost, newUser, newPass)
			#Drop the user first, then create it
			#Assume there is already an existing user w/ same name,
			#Drop it, then create it again

			dropUserQuery = "drop user {}@{}".format(newUser, newHost)
			results = cursor.execute(dropUserQuery)
			flushQuery = "flush privileges;"
			results = cursor.execute(flushQuery)
			
			#Create user again
			creation = "CREATE USER {}@{} IDENTIFIED BY '{}'".format(newUser, newHost, newPass)
			print(creation)
			results = cursor.execute(creation)
			return 0
		except Exception as e:
			print (e)
			return 1

	def runQuery(self):
		try:
			pass
		except Exception as e:
			print (e)

