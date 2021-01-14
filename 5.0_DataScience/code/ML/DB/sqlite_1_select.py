

#python2

import sys
import sqlite3

conn = sqlite3.connect('test.db')
print " Success !! Opened database";

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()

# exit the program
sys.exit()



------------------

