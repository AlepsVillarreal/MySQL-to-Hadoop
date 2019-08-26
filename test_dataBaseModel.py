import unittest
import sys
from dataBaseModel import dataBase

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
				#print(element)
				if userName in element:
					foundUser = True

			self.assertTrue(foundUser, "User: {} could not be created".format(userName))
		except Exception as e:
			print (e)

	def test_grantPriviledgesToUser(self, cursor, user):
		try:
			noPermission = False

			showUserQuery = 'select * from mysql.user where user = \'{}\';'.format(user)
			results = cursor.execute(showUserQuery)

			for element in cursor.fetchall():
				#print (element)
				if 'Y' in element:
					noPermission = True


			#Need to change criteria. Right now, only checking if there are any Y's in the mysql.users table
			self.assertTrue(noPermission, "User {} has some N's in his permissions")
					
		except Exception as e:
			print (e)

	def test_createDB(self, cursor, dbToLookFor):
		try:
			doesDbExist = False
			cursor.execute("SHOW DATABASES;")

			for element in cursor.fetchall():
				#print(element)
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
	#initializing test object and dataBase object
	testDB = test_main()
	rootDB = dataBase()
	#rootDB = dataBase('localhost', 'root', 'root')

	#Testing new DB connection
	rootDBConnection = rootDB.createConnection('root', 'root', 'localhost')
	testDB.test_createConnection(rootDBConnection)

	#Create new user
	newUserName = 'alex'
	newUserPassword = 'alex'
	newHostName = 'localhost'
	createUserCursor = rootDBConnection.cursor()
	rootDB.createUser(createUserCursor, newHostName, newUserName, newUserPassword)
	testDB.test_createUser(createUserCursor, newUserName)

	#Grant priviledges to recently created user
	grantPrivilegesCursor = rootDBConnection.cursor()
	rootDB.grantPriviledgesToUser(grantPrivilegesCursor, 'alex', 'localhost')
	checkPrivilegeCursor = rootDBConnection.cursor()
	testDB.test_grantPriviledgesToUser(checkPrivilegeCursor, 'alex')

	#Create new connection using newly created user
	newUserDBConnection = rootDB.createConnection('alex', 'alex', 'localhost')
	testDB.test_createConnection(newUserDBConnection)

	#Create the database
	dbName = 'sampledb'
	createDbCursor = newUserDBConnection.cursor()
	rootDB.createDB(createDbCursor, dbName)
	testDB.test_createDB(createDbCursor, dbName)

	#Create the tables for loading



	#Load the data to the tables