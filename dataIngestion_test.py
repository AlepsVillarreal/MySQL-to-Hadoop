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
			showUserQuery = 'select User from mysql.user;'.format(userName)

			results = createUserCursor.execute(showUserQuery)
			existingUsers = []
			for element in createUserCursor.fetchall():
				if userName in element:
					foundUser = True

			self.assertTrue(foundUser, "User: {} could not be created".format(userName))
		except Exception as e:
			print (e)

	def test_setPrivileges	(self, returnValue):
		try:
			pass
		except Exception as e:
			print (e)

	def test_createDB(self, returnValue):
		try:
			pass
			#Show DBs.
			#If DB name of assumed created DB exists, return True
			#assertRtnValue is True
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
	#Initializing newDB object
	newDB = dataBase('localhost', 'root', 'root')
	#Testing new DB connection
	newDBConnection = newDB.createConnection()
	testDB.test_createConnection(newDBConnection)

	#Create new user
	newUserName = 'alex'
	newUserPassword = 'alex'
	newHostName = 'localhost'
	createUserCursor = newDBConnection.cursor()
	rtnValue = newDB.createUser(createUserCursor, newHostName, newUserName, newUserPassword)
	testDB.test_createUser(createUserCursor, newUserName)

	#Create the database

	#Create the tables for loading

	#Load the data to the tables