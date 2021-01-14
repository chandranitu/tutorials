#python –jars /home/hadoop/J2EE_TRAINING/java/code/java8/lib/ojdbc14.jar
#driver="oracle.jdbc.driver.OracleDriver"
#url = "jdbc:oracle:thin:@localhost:1521:xe","system","oracle"

#sudo pip install cx_Oracle
#python2
#create table emp(id number,name varchar2(10));
#insert into emp values(1,'ch');
#insert into emp values(2,'ram');

import sys
import cx_Oracle

#connection
connection = cx_Oracle.connect('system/oracle@127.0.0.1/xe')

# prepare a cursor object using cursor() method
cursor = connection.cursor ()

print connection.version

# execute the SQL query using execute() method.
cursor.execute ("select * from emp")

# fetch all of the rows from the query
data = cursor.fetchall ()

# print the rows
for row in data:
print(row[0])
print (row[0], row[1])

# close the cursor object
cursor.close ()

# close the connection
connection.close ()

# exit the program
sys.exit()



------------------

