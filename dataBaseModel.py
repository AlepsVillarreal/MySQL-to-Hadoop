import mysql.connector
import sys
#inhouse

class dataBase(object):
	"""
	Database model class
	---------------------------------
	1. Creates users
	2. Grants permissions to user
	3. Creates a connection with a given user
	4. Creates a DB
	5. Creates a schema
	6. Loads info into tables
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

	def createTables(self, cursor, dbName):
		try:
			#Use the correct DB
			changeToDb = 'USE {};'.format(dbName)
			cursor.execute(changeToDb)

			#Drop the table if it exists
			dropTableQuery = "DROP TABLE IF EXISTS tempbycity;"
			cursor.execute(dropTableQuery)

			createTableQuery = "CREATE TABLE IF NOT EXISTS tempbycity (dt DATE, averageTemperature INT, averageTemperatureUncertainty INT, city varchar(50), country varchar(50), latitude varchar(50), longitude varchar(50))"
			cursor.execute(createTableQuery)

			describeTableQuery = "describe tempbycity;"
			results = cursor.execute(describeTableQuery)

			for result in cursor.fetchall():
				print(result)

		except Exception as e:
			print (e)

	def createDB(self, cursor, dbName):
		try:
			createDBQuery = cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(dbName))
			cursor.execute(createDBQuery)

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