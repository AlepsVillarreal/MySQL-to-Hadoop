import unittest
import sys
#from .. .. .. .. .. import main
#sys.path.append(r'C:\Users\alejandro.villarreal\Documents\Python Scripts\acnProject\python-virtual-environments')
from .. .. .. .. ..     main import dataBase

#Function that should return
class mySqlDBPreparing(unittest.TestCase):
    def test_createConnection(self, returnValue):
        #If it is able to connect, it will return 1. Otherwise, return 0
        try:
            newDB = dataBase('localhost', 'root', 'root')
            assertEquals(returnValue, 0, "The connection could not be established")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    print(sys.path)
    newDB = dataBase('localhost', 'root', 'root')
    print(newDB)
    #unittest.main()