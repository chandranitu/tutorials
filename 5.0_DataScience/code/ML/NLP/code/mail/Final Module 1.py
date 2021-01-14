""""
1.Create hive table Patient_Document sheet and load the data(refer attachment).
CREATE TABLE pat_document(id_src INT ,
createdby string ,
createddate date ,
modifiedby INT ,
modifieddate date ,
displaylocation string ,
documentname string ,
patient INT ,
practice INT ,
reviewcategory string ,
reviewcomment string ,
reviewstatus string ,
reviewedby string ,
revieweddate string ,
patdocumenttypedef INT ,
clinicalsignature INT ,
clinicalsignatureby string ,
clinicalsignaturedate string ,
responsibleuser string ,
dateofservice string ,
templateid string ,
draft INT ,
draftofpatdocument string ,
draftlastopeneddate string ,
draftlastautosaveddate string ,
patdocumentinternaltype string ,
draftlastmanualsaveddate string ,
draftlastopenedby string ,
owneruser string ,
usermanagedstatus string ,
extsourceid string ,
exturlbase string ,
exturlpath string ,
extcomment string ,
recipientlistinitialized string ,
esignuser string ,
esigndate string ,
esignsha256 string ,
patdocumentamendedstatus string ,
replacespatdocument string ,
replacedbypatdocument string ,
amendmentrequeststatus string ,
source string ,
amendmentrequestsource string ,
transferofcare string ,
deleted string ,
folder string ,
lobid string ,
lobfilepath string)
ROW FORMAT DELIMITED   
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

load data local  inpath '/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/7.NLP/code/mail/Patient_Document.csv' overwrite into table pat_document;
"""
# SQL statement to read the Hive table this needs to modify the filter as per the point 5	

sqlDf = sqlContext.sql('SELECT * FROM pat_document WHERE patient = "" )

# Combine base exturlbase and exturlpath to get Complete URL

df_url = sqlDf.rdd.map(lambda p: p.exturlbase + p.exturlpath).collect()

# This function reads the files from ISL server directory and create a list of file names. 

def download_file(url, seqnum):
    import urllib2
    import ssl
    count = 1
    print url
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    response = urllib2.urlopen(url, context=gcontext)
    
    filename = "pdf_file_" + str(seqnum) + "_.pdf" 
     k=list()
     for line in run_command(command):
    
        l=line.decode('utf8').split('/')
        k+=[l[-1].strip('\n')]
		
    list_filenames=k[1:]
    return list_filenames


# 2 Download the PDF files and stored in HBase Table as an Input Table.
"""
% hbase shell
hbase> create_namespace "mDNA"
hbase> create "mDNA:biomarker_unstructured_content", "extract"
"""
import csv
import happybase
import time

batch_size = 1000
host = "0.0.0.0"
host = "172.31.19.189"
file_path = "hdfs dfs -get /user/pdf/L8186-0510-1.pdf"
namespace = "mDNA1"
row_count = 0
start_time = time.time()
table_name = "biomarker_unstructured_content"
sock = socket.create_connection((host, 9090), timeout=30)
def connect_to_hbase():
    """ Connect to HBase server.
    This will use the host, namespace, table name, and batch size as defined in
    the global variables above.
    """
    conn = happybase.Connection('172.31.19.189')
    conn.open()
    table = conn.table('biomarker_unstructured_content')
    batch = table.batch(batch_size = batch_size)
    return conn, batch
###	
	table.put('namespace', {"extract":file_path, "Files": file_path})
					   
					   batch.put(row[0], { "data:kw": row[1], "data:sub": row[2], "data:type": row[3],
					   
###	
row = table.row(b'namespace')
print(row[b'family:extract'])
 try:
        connection.close()
    except Exception as e:
            print "Unable to close connection to hbase "
            print e
def insert_row(batch, row):
    """ Insert a row into HBase.
    Write the row to the batch. When the batch size is reached, rows will be
    sent to the database.
    """
    batch.put(patient,practice,TimeStamp,{ "extract:filename":list_filenames})

conn, batch = connect_to_hbase()
print "Connect to HBase. table name: %s, batch size: %i" % (table_name, batch_size)
csvreader, csvfile = read_csv()
print "Connected to file. name: %s" % (file_path)











