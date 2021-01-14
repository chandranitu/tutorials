

#python2

import sys
import cql

con= cql.connect(host="127.0.0.1",port=9160,keyspace="testKS")

cur=con.cursor()
result=cur.execute("select * from TestCF")
result.fetchone()
#result.fetch()


# exit the program
sys.exit()



------------------

