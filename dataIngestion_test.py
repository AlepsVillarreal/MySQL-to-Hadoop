import unittest
import sys
from main import dataBase

#Function that should return
class test_main(unittest.TestCase):
	def test_createConnection(self, returnValue):
		#If it is able to connect, it will return 1. Otherwise, return 0
		try:
			self.assertIsNot(returnValue, 1, "The connection could not be established")
		except Exception as e:
			print (e)

	def test_createUser(self, createUserCursor, userName):
		try:
			#Get user column from mysql.user table
			#If userName not in User column, return False. Else. True
			foundUser = False
			showUserQuery = 'select User from mysql.user;'

			results = createUserCursor.execute(showUserQuery)
			existingUsers = []
			for element in createUserCursor.fetchall():
				print(element)
				if userName in element:
					foundUser = True

			self.assertTrue(foundUser, "User: {} could not be created".format(userName))
		except Exception as e:
			print (e)

	def test_grantPriviledgesToUser(self, cursor, user):
		try:
			showUserQuery = 'select * from mysql.user;'
			results = cursor.execute(showUserQuery)

			for element in results.fetchall():
				print(element)

		except Exception as e:
			print (e)

	def test_createDB(self, cursor, dbToLookFor):
		try:
			doesDbExist = False

			results = cursor.execute("SHOW DATABASES;")
			for element in results:
				if dbToLookFor in element:
					doesDbExist = True

			self.assertTrue(doesDbExist, "database {} does not exist".format(dbToLookFor))

		except Exception as e:
			print (e)

	def test_createTables(self, returnValue):
		try:
			#Show Tables
			#If assumed table name does not show up in show tables
			pass
		except Exception as e:
			print (e)

	def test_loadData(self, returnValue):
		try:
			#If I know the amount of rows, check if count equals to that for each table created			
			pass
		except Exception as e:
			print (e)

if __name__ == '__main__':
	#print(sys.path)
	#initializing test object for main
	testDB = test_main()
	#Initializing rootDB object
	rootDB = dataBase()
	#rootDB = dataBase('localhost', 'root', 'root')
	#Testing new DB connection
	rootDBConnection = rootDB.createConnection('root', 'root', 'localhost')
	testDB.test_createConnection(rootDBConnection)

	#Create new user
	newUserName = 'alex'
	newUserPassword = 'alex'
	newHostName = 'localhost'
	print(type(rootDB))
	createUserCursor = rootDBConnection.cursor()
	rootDB.createUser(createUserCursor, newHostName, newUserName, newUserPassword)
	testDB.test_createUser(createUserCursor, newUserName)

	#Grant priviledges to recently created user
	grantPrivilegesCursor = rootDBConnection.cursor()
	showUserQuery = 'select User from mysql.user;'
	results = grantPrivilegesCursor.execute(showUserQuery)
	print(grantPrivilegesCursor)
	for result in results.fetchall():
		print (result) 
	rootDB.grantPriviledgesToUser(grantPrivilegesCursor, 'alex', 'localhost', 'mysql')
	checkPrivilegeCursor = rootDBConnection.cursor()
	testDB.test_grantPriviledgesToUser(checkPrivilegeCursor, 'alex')

	#Create new connection using newly created user
	newUserDBConnection = rootDB.createConnection('alex', 'alex', 'localhost')
	testDB.test_createConnection(newUserDBConnection)

	#Create the database
	dbName = 'sampleDB'

	#Create the tables for loading

	#Load the data to the tables