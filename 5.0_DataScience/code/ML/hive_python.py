#!/usr/bin/python

#pip install sasl
#pip install thrift
#pip install thrift-sasl
#pip install PyHive

from pyhive import hive
conn = hive.Connection(host="localhost", port=10000, username="root")

--------------------

import pyhs2

with pyhs2.connect(host='localhost',
               port=10000,
               authMechanism="PLAIN",
               user='root',
               password='test',
               database='default') as conn:
    with conn.cursor() as cur:
        #Show databases
        print cur.getDatabases()

        #Execute query
        cur.execute("select * from table")

        #Return column info from query
        print cur.getSchema()

        #Fetch table results
        for i in cur.fetch():
            print i

--------------

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
try:
    transport = TSocket.TSocket('<node-with-metastore>', 9083)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = ThriftHive.Client(protocol)
    transport.open()
    client.execute("CREATE TABLE test(c1 int)")

    transport.close()
except Thrift.TException, tx:
    print '%s' % (tx.message)
