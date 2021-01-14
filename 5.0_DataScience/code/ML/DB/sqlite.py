

#python2


import sys
import sqlite3

conn = sqlite3.connect('test.db')

print " Success !! Opened database";

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),SALARY REAL);''')

print "Table created successfully";

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'chandra', 32, 'delhi', 23000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'nitu', 25, 'patna', 55000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'ram', 23, 'goa', 60000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'shayam', 25, 'kolkata ', 45000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (5, 'NIIT', 25, 'Noida ', 75000.00 )");
conn.commit()


conn.close()



# exit the program
sys.exit()



------------------

