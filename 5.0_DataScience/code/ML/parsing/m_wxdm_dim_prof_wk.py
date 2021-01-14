###----------------------------------------------------------------------------
### Name        : m_wxdm_dim_prof_wk.py
###
###
### Purpose     : Perform the following tasks:
###               1. Source file is fixed with format, that has to be written in target after processing.
###               
###
###    Who                                When           What
### ----------------------------     ----------     -------------------------------
### XYZ Development Team                  10 September       2017     Created
###----------------------------------------------------------------------------

# Section for importing PySpark libraries
import os
import time
import datetime
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql import SQLContext 
from pyspark.conf import SparkConf
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.functions import lit
from pyspark.sql.functions import col
from pyspark.sql import functions as F

spark=SparkSession.builder.master("yarn").appName("m_wxdm_dim_prof").config(conf=SparkConf()).getOrCreate()
sc=spark.sparkContext
sqlContext = SQLContext(sc)

DATA_SRC_ID=int(os.environ["DataSrcID"])
DATA_CYCLE_DT=os.environ["DATA_CYCLE_DT"]
CRTN_DT=time.strftime("%x")
LAST_UPDT_DT=time.strftime("%x")
S3_DATA_DIR=os.environ["S3_DATA_DIR"]
SCHEMA_PMR_STAGE=os.environ["SCHEMA_PMR_STAGE"]
S3_LANDING=os.environ["S3_LANDING"]

#Source File
src_dim_main=str(S3_LANDING)+'/PMR_WXDM_DIM_PROF'
dim_prof_wk=str(S3_DATA_DIR)+str(SCHEMA_PMR_STAGE)+'/PROF_WK'

#target file
dim_prof_tar=str(S3_DATA_DIR)+str(SCHEMA_PMR_STAGE)+'/M_WXDM_DIM_PROF_WK'

rdd=sc.textFile(src_dim_main)
rdd_src=rdd.map(lambda x: (x[:2],x[2:30]))
rdd1= rdd_src.map(lambda x: (x[0].strip(),x[1].strip()))

schema=StructType([
	StructField("SRC_VNDR_PROF_ID",StringType(),True),	
	StructField("SRC_PROF_NM",StringType(),True)				
	])
	
df_src=rdd1.toDF(schema=schema)

# Getting Maximum ID from source table
df_wk=spark.read.parquet(dim_prof_wk).filter(col("DATA_SRC_ID")== DATA_SRC_ID)

MAX_PROF_ID=int(df_wk.groupby("PROF_ID").agg({"PROF_ID":"max"}).first()[0])+1

df_join=df_wk.join(df_src,df_wk.VNDR_PROF_ID==df_src.SRC_VNDR_PROF_ID,"fullouter")


# Only Update and insert will take place during below operation.
#u-update - if existing record is coming in source , update will take place
#i- insert - if new record comes in source
#e- existing - if there record which is in target does n't match with source . No change in target


df_flag=df_join.withColumn("type",when(col("VNDR_PROF_ID")==col("SRC_VNDR_PROF_ID"),'u').when(col("SRC_VNDR_PROF_ID").isNull(),'e').otherwise('i'))

df_e = df_flag.filter(df_flag.type=='e').select("DATA_SRC_ID","DATA_CYCLE_DT","VNDR_PROF_ID","PROF_NM","CRTN_DT","LAST_UPDT_DT","PROF_ID")

# update creation date("crtn_dt") from target for records that are updated

df_u = df_flag.filter(df_flag.type=='u').select(lit(DATA_SRC_ID).alias('DATA_SRC_ID'),to_date(from_unixtime(unix_timestamp(lit(DATA_CYCLE_DT),'MM/dd/yyyy'), 'yyyy-MM-dd')).alias("DATA_CYCLE_DT"),"SRC_VNDR_PROF_ID","SRC_PROF_NM",lit(CRTN_DT).alias('CRTN_DT'),lit(LAST_UPDT_DT).alias('LAST_UPDT_DT'),'PROF_ID')

df_i1 = df_flag.filter(df_flag.type=='i').select(lit(DATA_SRC_ID).alias('DATA_SRC_ID'),to_date(from_unixtime(unix_timestamp(lit(DATA_CYCLE_DT),'MM/dd/yyyy'), 'yyyy-MM-dd')).alias("DATA_CYCLE_DT"),"SRC_VNDR_PROF_ID","SRC_PROF_NM",lit(CRTN_DT).alias('CRTN_DT'),lit(LAST_UPDT_DT).alias('LAST_UPDT_DT'))

newSchema = StructType([StructField("uuid", IntegerType(), False)]+ df_i1.schema.fields)
df_i2 = df_i1.rdd.zipWithIndex().map(lambda (row, id): {k:v for k, v in row.asDict().items() + [("uuid", id)]}).toDF(newSchema)
df_i3 = df_i2.withColumn("PROF_ID",df_i2["uuid"]+lit(MAX_PROF_ID)).drop("uuid")


df_upsert=df_e.union(df_i3).union(df_u)
#df_upsert.cache()

print(df_upsert.show())

# writting to target file
df_upsert.write.parquet(dim_prof_tar,mode="append")

sc.stop()
