import csv
import happybase
import time
host = "NN"
file_path = "hdfs dfs -get /user/pdf/L8186-0510-1.pdf"
namespace = "mDNA"
row_count = 0
start_time = time.time()
table_name = "biomarker_unstructured_content"
def connect_to_hbase():
    """ Connect to HBase server.
    This will use the host, namespace, table name, and batch size as defined in
    the global variables above.
    """
    conn = happybase.Connection(host = host,
        table_prefix = namespace,
        table_prefix_separator = ":")
    conn.open()
    table = conn.table(table_name)
 #   batch = table.batch(batch_size = batch_size)
    return conn, batch
	
sc.parallelize(table.put("record1", { "extract: "name4"}))
conn.close()
rdd = sc.binaryFiles(file_path)
rdd1 = rdd.collect(10)
rdd1 =rdd_files.map(process_data).collect(10)


def transfer_from_hdfs():
    command = 'hadoop fs -ls /user/pdf'.split()
    k=list()

    for line in run_command(command):
		l=line.decode('utf8').split('/')
		k+=[l[-1].strip('\n')]
		list_filenames=k[1:]
    return list_filenames