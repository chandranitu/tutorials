#!/usr/bin/python
#sudo pip install MySQL-python -t
#python2
#create table login(id int,name string,file blob);

import sys
import mysql.connector
from mysql.connector import MySQLConnection, Error
#from python_mysql_dbconfig import read_db_config

connection=mysql.connector.connect(host='localhost',database='test',user='root',password='root')

# prepare a cursor object using cursor() method
cursor = connection.cursor ()
cursor.execute ("select * from login")


def file_writer(id,name,path):
   	#sql = "INSERT INTO login VALUES({},{},{})".format(id,name,path) 
	#sql = "INSERT INTO login (id,name) VALUES (%s, %s)"        	
        cursor.execute("INSERT INTO login VALUES (%s, %s, %s)", (id, name,path))
	#cursor.execute(sql)
	connection.commit()

#val = (3, "nitu1","/home/hadoop/mmu.txt")
path="/home/hadoop/mmu.txt"
file_writer(1,"nitu1",path)

# close the cursor object
cursor.close ()

# close the connection
connection.close ()

# exit the program
sys.exit()

---------

