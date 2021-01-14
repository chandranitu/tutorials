pyspark --jars /opt/cloudera/parcels/CDH-5.10.0-1.cdh5.10.0.p0.41/lib/spark/lib/spark-examples-1.6.0-cdh5.10.0-hadoop2.6.0-cdh5.10.0.jar,/opt/cloudera/parcels/CDH-5.10.0-1.cdh5.10.0.p0.41/lib/hbase/lib/hbase-examples-1.2.0-cdh5.10.0.jar

pyspark --jars /opt/cloudera/parcels/CDH-5.10.0-1.cdh5.10.0.p0.41/lib/spark/lib/spark-examples-1.6.0-cdh5.10.0-hadoop2.6.0-cdh5.10.0.jar,/opt/cloudera/parcels/CDH-5.10.0-1.cdh5.10.0.p0.41/lib/hbase/lib/hbase-examples-1.2.0-cdh5.10.0.jar

host = 'NN'  
table = 't1'  
port = '2181'
keyConv = "org.apache.spark.examples.pythonconverters.StringToImmutableBytesWritableConverter"  
valueConv = "org.apache.spark.examples.pythonconverters.StringListToPutConverter"  
conf = {"hbase.zookeeper.quorum": host, "hbase.mapred.outputtable": table, "mapreduce.outputformat.class": "org.apache.hadoop.hbase.mapreduce.TableOutputFormat","mapreduce.job.output.key.class": "org.apache.hadoop.hbase.io.ImmutableBytesWritable", "mapreduce.job.output.value.class": "org.apache.hadoop.io.Writable"}  
cmdata_conf = {"hbase.zookeeper.property.clientPort":port, "hbase.zookeeper.quorum": host}
cmdata_rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat","org.apache.hadoop.hbase.io.ImmutableBytesWritable","org.apache.hadoop.hbase.client.Result",keyConverter=keyConv,valueConverter=valueConv,conf=cmdata_conf)
output = cmdata_rdd.collect()

put 't1', 'Info', 'Age', '12', ts1


cmdata_rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat","org.apache.hadoop.hbase.io.ImmutableBytesWritable","org.apache.hadoop.hbase.client.Result",keyConverter=keyConv,valueConverter=valueConv,conf=cmdata_conf)

host = 'NN'  
table = 't1'  
keyConv = "org.apache.spark.examples.pythonconverters.StringToImmutableBytesWritableConverter"  
valueConv = "org.apache.spark.examples.pythonconverters.StringListToPutConverter"  
conf = {"hbase.zookeeper.quorum": host, "hbase.mapred.outputtable": table, "mapreduce.outputformat.class": "org.apache.hadoop.hbase.mapreduce.TableOutputFormat","mapreduce.job.output.key.class": "org.apache.hadoop.hbase.io.ImmutableBytesWritable", "mapreduce.job.output.value.class": "org.apache.hadoop.io.Writable"}  
newpeople=sc.parallelize([('xyz',['userid3','info','Age','NewUser'])])
newpeople.saveAsNewAPIHadoopDataset(conf=conf,keyConverter=keyConv,valueConverter=valueConv)


