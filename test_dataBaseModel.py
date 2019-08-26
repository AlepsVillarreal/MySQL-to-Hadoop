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

	def test_createTables(self, cursor, dictOfTables, dbName):
		try:
			#This method will check for the existence of the appropriate tables/columns
			error_createTables_tables = False
			err_Tables = []
			error_createTables_columns = False
			err_Columns = []

			useDbQuery = 'USE {};'.format(dbName)
			cursor.execute(useDbQuery)

			checkTablesQuery = 'SHOW TABLES;'
			cursor.execute(checkTablesQuery)

			#Check if tables were actually created
			for table in cursor.fetchall():
				print('ALL TABLES')
				print(table)
				if table not in dictOfTables:
					err_Tables.append(table)
					error_createTables_tables = True

			#For all tables from the valid tables, get the columns
			for table in dictOfTables.keys():
				getColumnsOfTableQuery = "SHOW COLUMNS FROM {};".format(table)
				tableColumns = cursor.execute(getColumnsOfTableQuery)
				#for all actual columns
				for column in cursor.fetchall():
					print('ALL COLUMNS OF TABLE {}'.format(table))
					print(column)
					#Check if the column is inside the list that is the value of the dictOfTables dictionary.
					#If it's not there, one column is not there
					if column not in dictOfTables['table']:
						err_Columns.append(column)
						error_createTables_columns = True

			self.assertFalse(error_createTables_tables, "Error while creating the tables of {}".format(err_Tables))
			self.assertFalse(error_createTables_columns, "Error while creating the columns of {}".format(err_Columns))

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
	dictOfTables = {}
	dictOfTables['tempbycity'] = ['dt', 'AverageTemperature', 'AverageTemperatureUncertainty', 
	'City', 'Country', 'Latitude', 'Longitude']
	createTableCursor = newUserDBConnection.cursor()
	rootDB.createTables(createTableCursor, dbName)
	testDB.test_createTables(createTableCursor, dictOfTables, dbName)

	#Load the data to the tables