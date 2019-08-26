import mysql.connector
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
	def __init__(self, ):
		pass

	@staticmethod
	def createConnection(userName, passwd, hostValue):
		try:
			mydb = mysql.connector.connect(
			  host=hostValue,
			  user=userName,
			  passwd=passwd
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
			creation = "CREATE USER IF NOT EXISTS {}@{} IDENTIFIED BY '{}'".format(newUser, newHost, newPass)
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

	def createDB(self, cursor, dbName):
		try:
			createDBQuery = cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(dbName))
			results = cursor.execute(createDBQuery).fetchall()

		except Exception as e:
			print (e)

	def grantPriviledgesToUser(self, cursor, userName, hostName):
		try:
			query = "GRANT ALL PRIVILEGES ON *.* TO '{}'@'{}';".format(userName, hostName)
			results = cursor.execute(query)

			flushQuery = "FLUSH PRIVILEGES;"
			flushResults = cursor.execute(flushQuery)
		except Exception as e:
			print (e)
			return 1