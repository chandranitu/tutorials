############################################################################################################################################
# 
##############################################################################################################################################
#
# Below mentioned is the command to submit -
# spark-submit  --jars /opt/cloudera/parcels/CDH/jars/spark-examples-1.6.0-cdh5.7.3-hadoop2.6.0-cdh5.7.3.jar,/opt/cloudera/parcels/CDH/jars/hbase-examples-1.2.0-cdh5.7.3.jar \
#       --conf "spark.executor.extraClassPath=$(hbase classpath)" \
#      --conf "spark.driver.extraClassPath=$(hbase classpath)" \
#	   --master yarn --driver-memory 10G --executor-memory 30G --executor-cores 6 --num-executors 20 \
#         mDNA_Biomarker_Module3_NLP_v4.y
#	  
		  

from __future__ import print_function
import time
from time import gmtime, localtime,strftime
from ctypes import *
from pyspark.context import SparkContext
from pyspark.sql import HiveContext
from pyspark.sql import SQLContext
from py4j.protocol import Py4JJavaError
import datetime
import re, sys, os

# Regular expressions of all the variables to be extracted from OCR Text. 
Name_regex1 = r'Name.{1,30}'
Name_regex2 = r'Name'
Name_regex3 = r'([A-Z][a-z]*)'
space_l = ''
DOB_regex1 = r'of\sBirth:.{1,17}'
DOB_regex2 = r'of Birth'
Date_regex = r'[^a-zA-Z0-9]+'
Gender_regex1 = r'Gender:\s.{1,10}'
Gender_regex2 = 'Gender'
Gender_regex3 = r'Male|Female'
SpeType_regex1 = r'Specimen\sType:\s.{1,10}'
SpeType_regex2 = 'Specimen Type'
SpeType_regex3 = r'Blood|Buccal Wash'
SpeDate_regex1 = r'Draw\sDate:.{1,15}'
SpeDate_regex2 = 'Draw Date'
Reportdt_regex1 = r'Report\sDate:\s.{1,15}'
Reportdt_regex2 = 'Report Date'
Accdt_regex1 = r'Accession\sDate:\s.{1,15}'
Accdt_regex2 = 'Accession Date'
NotFound = "NotFound"
NotApplicable = 'NotApplicable'

Intprt_cat1_regex1 = r"((?:[A-Z\d]{1,}\s[A-Z\d]{1,}\s?){1,})(?:\s?[^A-Z]+[tesTES]{4}\s?(?:[perfomdPERFOMD]{9})?)"
Intprt_cat1_regex2 = r'(?:^.{1,1000}I[NTERPAIO]{12}NN?)(.{1,260}[ISCLTED]{5})'
Intprt_cat1_regex3 = r'(?:[isclted]{7}.)(.{1,50}[isclted]{5})'
Intprt_cat1_regex4 = r'[^a-zA-Z\s]+'

Intprt_cat2_regex1 = r'Interpretation.{1,100}'

Intprt_cat3_regex1 = r'(?:RESULT.)(.{1,150}).(Note|Detai)'

cat1_line = r"(?:^.{1,1000}I[NTERPAIO]{12}NN?)(.{1,260}[CLTED]{5})"
cat1_test1 = r"(^.{1,50}[ING]{3})(?:.{1,60}[CLTED]{5}\s?)(.{1,31})\s"
cat1_test2 = r"[CLTED]{5}.+(B[RCAZO]{3,6}.{1,}[ING]{3})"
cat1_result1 = r"[ING]{3}\s([a-zA-Z\s]{1,20}[CLTED]{5})"
cat1_result2 = r"[CLTED]{5}.+B[RCAZO]{3,6}.{1,}[ING]{3}.{1,40}?(.+[A-Z\s][CLTED]{5})\s"

cat2_test1 = r"(?:n'?\s?(?:.+-\s)?)(BRCO?A[1-2]?Z?)(?:.+BRCO?A[1-2]?Z?\s(?:~\s)?)"
cat2_test2 = r"(?:BRCO?A[1-2]?Z?.+n)(BRCO?A[1-2]?Z?)(?:\s)"
cat2_result1 = r"(?:BRCO?A[1-2]?Z?\s(?:~\s)?)(\w+(?:\s\w+)?)(?:(?:\s\S)?nBRC)"
cat2_result2 = r"(?:BRCO?A[1-2]?Z?\s(?:~\s)?)(\w+(?:\s\w+)?)(?:n(?:\.\s)?Interpretationn)"

cat3_test_px = r"(?:.+RESULT:\s)(.+)(?:nNote.+)"
cat3_test_sx = r"(?:.+FINDINGS:\s)(.+)(?:n(?:\w+\s)?Details.+)"


Arr_Template_regex=[]
Arr_Template_regex.append(r'(?:B?R[A-Z][A-Z]?A[a-zA-Z0-9~@#$^*!()_+=[\]{}|\\,.?: -]{0,3}.a?n?d?.[A-Z]?B?RC[aA][A-Z0-9]{0,4}.An[a-z][A-Za-z][yY][sS][a-z][a-z]\s?Res?u?[lt]{0,2}?)')
Arr_Template_regex.append(r'Large Rearrangement Analysis Result')
Arr_Template_regex.append(r'Three Mutation BRCA1')
Arr_Template_regex.append(r'Gene-Specific BRACAnalysis')
Arr_Template_regex.append(r'Gene Sequence Result')
Arr_Template_regex.append(r'Gene Analysis Result')
Arr_Template_regex.append(r'Gene Sequence Analysis Result')
Arr_Template_regex.append(r'Genetic Test Result')
Arr_Template_regex.append(r'myRisk Genetic Result')
Arr_Template_regex.append(r'6 High-Risk Hereditary')
Arr_Template_regex.append(r'17 Genes Associated')
Arr_Template_regex.append(r'28 Genes Associated')
Arr_Template_regex.append(r'23 Genes Associated')
Arr_Template_regex.append(r'24 Genes Associated')
Arr_Template_regex.append(r'Oncology Genetic Test Report')
Arr_Template_regex.append(r'Comprehensive BRCA1/2 Analysis')
Arr_Template_regex.append(r'Myriad Accession Number')
Arr_Template_regex.append(r'Single Site Analysis Result')
Arr_Template_regex.append(r'Invitae')

Arr_Attr_Template=[]
Arr_Attr_Template.append(['Category1','BRACAnalysis CDx FDA Approved BRCA1 and BRCA2 Analysis Result','Myriad'])
Arr_Attr_Template.append(['Category1','BRACAnalysis Rearrangement Test Full Gene BRCA1-BRCA2 Large Rearrangement Analysis Result','Myriad'])
Arr_Attr_Template.append(['Category1','Multisite 3 BRACAnalysis Three Mutation BRCA1 and BRCA2 Analysis for Ashkenazi Individuals','Myriad'])
Arr_Attr_Template.append(['Category1','Gene-Specific BRACAnalysis BRCA1 Analysis Result','Myriad'])
Arr_Attr_Template.append(['Category2','BRACAnalysis Comprehensive BRCA1-BRCA2 Gene Sequence Result','Myriad'])
Arr_Attr_Template.append(['Category2','BRACAnalysis Comprehensive BRCA1-BRCA2 Gene Analysis Result','Myriad'])
Arr_Attr_Template.append(['Category2','BRACAnalysis Comprehensive BRCA1-BRCA2 Gene Sequence Analysis Result','Myriad'])
Arr_Attr_Template.append(['Category3','Genetic Test Result','Myriad myRisk'])
Arr_Attr_Template.append(['Category3','myRisk Genetic Result','Myriad myRisk'])
Arr_Attr_Template.append(['Category4','BRCAplus: Analyses of 6 High-Risk Hereditary Breast Cancer Genes','Ambry Genetics'])
Arr_Attr_Template.append(['Category4','BreastNext: Anlyses of 17 Genes Associated with Hereditary Breast Cancer','Ambry Genetics'])
Arr_Attr_Template.append(['Category4','CancerNext: Analyses of 28 Genes Associated with Hereditary Cancer','Ambry Genetics'])
Arr_Attr_Template.append(['Category4','OvaNext: Analyses of 23 Genes Associated with Hereditary Ovarian Cancer','Ambry Genetics'])
Arr_Attr_Template.append(['Category4','OvaNext: Analyses of 24 Genes Associated with Hereditary Ovarian Cancer','Ambry Genetics'])
Arr_Attr_Template.append(['Category5','Oncology Genetic Test Report','Gene Dx'])
Arr_Attr_Template.append(['Category6','Comprehensive BRCA1/2 Analysis','Integrated Genetics'])
Arr_Attr_Template.append(['Category7','BRACAnalysis Genetic Variant of Uncertain Clinical Significance','Myriad'])
Arr_Attr_Template.append(['Category7','Single Site Analysis Result','Myriad'])
Arr_Attr_Template.append(['Category8','Invitae','Invitae'])

# Regular expressions of all the variables to be extracted from OCR Text. 
Name_Pat1 = re.compile(Name_regex1)
Name_Pat2 = re.compile(Name_regex2)
Name_Pat3 = re.compile(Name_regex3)
DOB_Pat1  = re.compile(DOB_regex1)
DOB_Pat2  = re.compile(DOB_regex2)
Date_Pat1 = re.compile(Date_regex)
Gender_Pat1 = re.compile(Gender_regex1)
Gender_Pat2 = re.compile(Gender_regex2)
Gender_Pat3 = re.compile(Gender_regex3)
SpeType_Pat1 = re.compile(SpeType_regex1)
SpeType_Pat2 = re.compile(SpeType_regex2)
SpeType_Pat3 = re.compile(SpeType_regex3)
SpeDate_Pat1 = re.compile(SpeDate_regex1)
SpeDate_Pat2 = re.compile(SpeDate_regex2)
Reportdt_Pat1 = re.compile(Reportdt_regex1)
Reportdt_Pat2 = re.compile(Reportdt_regex2)
Accdt_pat1 = re.compile(Accdt_regex1)
Accdt_pat2 = re.compile(Accdt_regex2)

Intprt_cat1_pat1 = re.compile(Intprt_cat1_regex1)
Intprt_cat1_pat2 = re.compile(Intprt_cat1_regex2, re.IGNORECASE)
Intprt_cat1_pat3 = re.compile(Intprt_cat1_regex3, re.IGNORECASE)
Intprt_cat1_pat4 = re.compile(Intprt_cat1_regex4)

Intprt_cat2_pat1 = re.compile(Intprt_cat2_regex1)
Intprt_cat3_pat1 = re.compile(Intprt_cat3_regex1, re.IGNORECASE)

cat1_line_pat = re.compile(cat1_line, re.IGNORECASE)
cat1_test1_pat = re.compile(cat1_test1, re.IGNORECASE)
cat1_test2_pat = re.compile(cat1_test2, re.IGNORECASE)
cat1_result1_pat = re.compile(cat1_result1, re.IGNORECASE)
cat1_result2_pat = re.compile(cat1_result2, re.IGNORECASE)

cat2_test1_pat = re.compile(cat2_test1, re.IGNORECASE)
cat2_test2_pat = re.compile(cat2_test2, re.IGNORECASE)
cat2_result1_pat = re.compile(cat2_result1, re.IGNORECASE)
cat2_result2_pat = re.compile(cat2_result2, re.IGNORECASE)

cat3_test_px_pat = re.compile(cat3_test_px, re.IGNORECASE)
cat3_test_sx_pat = re.compile(cat3_test_sx, re.IGNORECASE)

Arr_Template_pat=[]
#for index, Template_regex in enumerate(Arr_Template_regex):
for Template_regex in Arr_Template_regex:
	Template_pat=re.compile(Template_regex)
	Arr_Template_pat.append(Template_pat)

# To extract First Name of Patient from OCR Text
def get_FirstName_pat1(all_lines):
    Name = Name_Pat1.search(all_lines)
    try:
        Name1 = Name.group()
        Name2 = Name_Pat2.sub(space_l, Name1)
        Name3 = Name_Pat3.findall(Name2)
        FirstName = str(Name3[1])
    except:
        FirstName = NotFound
    return FirstName

# To extract Last Name of Patient from OCR Text
def get_Last_Name_pat1(all_lines):
    LName = Name_Pat1.search(all_lines)
    try:
        LName1 = LName.group()
        LName2 = Name_Pat2.sub(space_l, LName1)
        LName3 = Name_Pat3.findall(LName2)
        LastName = str(LName3[0])
    except:
        LastName = NotFound
    return LastName

# To extract DOB of Patient from OCR Text.
def get_DOB_pat1(all_lines):
    DOB = DOB_Pat1.search(all_lines)
    try:
        DOB1 = str(DOB_Pat2.sub(space_l, DOB.group()))
        DOB2 = Date_Pat1.sub(space_l, DOB1)
        Date_of_Birth = str(DOB2[0:3] + ' ' + DOB2[3:5] + ',' + DOB2[5:9])
    except:
        Date_of_Birth = NotFound
    return Date_of_Birth

# To extract Gender of Patient from OCR Text
def get_gender_pat1(all_lines):
    G1 = Gender_Pat1.search(all_lines)
    try:
        G2 = Gender_Pat2.sub(space_l, G1.group())
        G3 = Gender_Pat3.search(G2)
        G4 = str(G3.group())
    
        Gender = G4
    except:
        Gender = NotFound
    return Gender

# To extract Speciman Type from OCR Text
def get_SpecimenType_pat1(all_lines):
    S1 = SpeType_Pat1.search(all_lines)
    try:
        S2 = SpeType_Pat2.sub(space_l, S1.group())
        S3 = SpeType_Pat3.search(S2)
        s4 = str(S3.group())
    
        Specimen_Type = s4
    except:
        Specimen_Type = NotFound
    return Specimen_Type

# To extract Speciman Date from OCR Text
def get_SpecimenDate_pat1(all_lines):
    
    SD1 = SpeDate_Pat1.search(all_lines)
    try:
        SD2 = str(SpeDate_Pat2.sub(space_l, SD1.group()))
        SD3 = Date_Pat1.sub(space_l, SD2)
        Specimen_Date = str(SD3[0:3] + ' ' + SD3[3:5] + ',' + SD3[5:9])
    except:
        Specimen_Date = NotFound
    return Specimen_Date

# To extract Report Date from OCR Text
def get_ReportDate_pat1(all_lines):
    
    R1 = Reportdt_Pat1.search(all_lines)
    try:
        R2 = str(Reportdt_Pat2.sub(space_l, R1.group()))
        R3 = Date_Pat1.sub(space_l, R2)
    
        Report_Date = str(R3[0:3] + ' ' + R3[4:5] + ',' + R3[5:9])
    except:
        Report_Date = NotFound
    return Report_Date


# To extract Accession Date from OCR Text
def get_AccessionDate_pat1(all_lines):
    
    A1 = Accdt_pat1.search(all_lines)
    try:
        A2 = str(Accdt_pat2.sub(space_l, A1.group()))
        A3 = Date_Pat1.sub(space_l, A2)
        Accession_Date = str(A3[0:3] + ' ' + A3[3:5] + ',' + A3[5:9])
    except:
        Accession_Date = NotFound
    return Accession_Date

def get_interpretation_cat1(all_lines):
	result = NotFound
	try:
		result = Intprt_cat1_pat1.search(all_lines).group(1)
	except:
		result = NotFound
	
	if result == NotFound:
		line = Intprt_cat1_pat2.search(all_lines)
		try:
			test = Intprt_cat1_pat3.search(line.group(1))
			result = Intprt_cat1_pat4.sub(space_l, test.group(1))
		except:
			result = NotFound 
	return result

def get_interpretation_cat2(all_lines):
	line = line = Intprt_cat2_pat1.search(all_lines)
	try:
		result = line.group()
	except:
		result = NotFound
	return result

def get_interpretation_cat3(all_lines):
	line = Intprt_cat3_pat1.search(all_lines)
	try:
		result = line.group(1)
	except:
		result = NotFound
	return result

def get_test1_cat1(all_lines):
	line = cat1_line_pat.search(all_lines)
	try:
		test1 = cat1_test1_pat.search(line.group(1))
		result = test1.group(1)
		if len(test1.groups()) > 1:
			result = result + " " + test1.group(2)
	except:
		result = NotFound
	print (result)
	return result

def get_test2_cat1(all_lines):
	test2 = cat1_test2_pat.search(all_lines)
	try:
		result = test2.group(1)
		if len(test2.groups()) > 1:
			result = result + " " + test2.group(2)
	except:
		result = NotFound
	return result

def get_result1_cat1(all_lines):
	result1 = cat1_result1_pat.search(all_lines)
	try:
		result = result1.group(1)
		if len(result1.groups()) > 1:
			result = result + " " + result1.group(2)
	except:
		result = NotFound
	return result

def get_result2_cat1(all_lines):
	result2 = cat1_result2_pat.search(all_lines)
	try:
		result = result2.group(1)
		if len(result2.groups()) > 1:
			result = result + " " + result2.group(2)
	except:
		result = NotFound
	return result

def get_test1_cat2(all_lines):
	test1 = cat2_test1_pat.search(all_lines)
	try:
		result = test1.group(1)
	except:
		result = NotFound
	return result

def get_test2_cat2(all_lines):
	test2 = cat2_test2_pat.search(all_lines)
	try:
		result = test2.group(1)
	except:
		result = NotFound
	return result

def get_result1_cat2(all_lines):
	result1 = cat2_result1_pat.search(all_lines)
	try:
		result = result1.group(1)
	except:
		result = NotFound
	return result

def get_result2_cat2(all_lines):
	result2 = cat2_result2_pat.search(all_lines)
	try:
		result = result2.group(1)
	except:
		result = NotFound
	return result

def get_result_cat3(all_lines):
	result_px = cat3_test_px_pat.search(all_lines)
	result_sx = cat3_test_sx_pat.search(all_lines)
	try:
		result = result_px.group(1) + '\n' + result_sx.group(1)
	except:
		result = NotFound
	return result


# To extract Patient Details, Test and Result of medical report(OCR Text) 
def get_Patient_Details(all_lines,Attr_Template):
	First_Name = NotFound
	Last_Name = NotFound
	DOB = NotFound
	Gender = NotFound
	SpecimenType = NotFound
	SpecimenDate = NotFound
	ReportDate = NotFound
	AccessionDate = NotFound
	Interpretation = NotFound
	test1 = NotFound
	test2 = NotFound
	Result1 = NotFound
	Result2 = NotFound
	
	Catdetails=[]
	if Attr_Template[0] == 'Category1':
		First_Name = get_FirstName_pat1(all_lines)
		Last_Name = get_Last_Name_pat1(all_lines)
		DOB = get_DOB_pat1(all_lines)
		Gender = get_gender_pat1(all_lines)
		SpecimenType = get_SpecimenType_pat1(all_lines)
		SpecimenDate = get_SpecimenDate_pat1
		ReportDate = get_ReportDate_pat1(all_lines)
		AccessionDate = get_AccessionDate_pat1(all_lines)
		Interpretation=get_interpretation_cat1(all_lines)
		test1=get_test1_cat1(all_lines)
		test2=get_test2_cat1(all_lines)
		Result1 = get_result1_cat1(all_lines)
		Result2 = get_result2_cat1(all_lines)
	elif Attr_Template[0] == 'Category2':
		First_Name = get_FirstName_pat1(all_lines)
		Last_Name = get_Last_Name_pat1(all_lines)
		DOB = get_DOB_pat1(all_lines)
		Gender = get_gender_pat1(all_lines)
		SpecimenType = get_SpecimenType_pat1(all_lines)
		SpecimenDate = get_SpecimenDate_pat1
		ReportDate = get_ReportDate_pat1(all_lines)
		AccessionDate = get_AccessionDate_pat1(all_lines)
		Interpretation=get_interpretation_cat2(all_lines)
		test1=get_test1_cat2(all_lines)
		test2=get_test2_cat2(all_lines)
		Result1 = get_result1_cat2(all_lines)
		Result2 = get_result2_cat2(all_lines)
	elif Attr_Template[0] == 'Category3':
		First_Name = get_FirstName_pat1(all_lines)
		Last_Name = get_Last_Name_pat1(all_lines)
		DOB = get_DOB_pat1(all_lines)
		Gender = get_gender_pat1(all_lines)
		SpecimenType = get_SpecimenType_pat1(all_lines)
		SpecimenDate = get_SpecimenDate_pat1
		ReportDate = get_ReportDate_pat1(all_lines)
		AccessionDate = get_AccessionDate_pat1(all_lines)
		Interpretation=get_interpretation_cat3(all_lines)
		test1 = NotFound
		test2 = NotFound
		Result1 = get_result_cat3(all_lines)
		Result2 = NotFound
	try:
		Pat_details.append(First_Name)
		Pat_details.append(Last_Name)
		Pat_details.append(DOB)
		Pat_details.append(Gender)
		Pat_details.append(SpecimenType)
		Pat_details.append(SpecimenDate)
		Pat_details.append(ReportDate)
		Pat_details.append(AccessionDate)
		Pat_details.append(Interpretation)
		Pat_details.append(test1)
		Pat_details.append(test2)
		Pat_details.append(Result1)
		Pat_details.append(Result2)
	except:
		sys.stderr.write("Error occurred while preparing Pat_details append data")
	print (Pat_details)
	return Pat_details

# To extract attributes the Report(OCR Text) - category number, template name, company name and Interpretation.
def get_attr_code(all_lines):
	tmp_list = []
	Patient_Details = []
	First_Name = NotApplicable
	Last_Name = NotApplicable
	DOB = NotApplicable
	Gender = NotApplicable
	SpecimenType = NotApplicable
	SpecimenDate = NotApplicable
	ReportDate = NotApplicable
	AccessionDate = NotApplicable
	Interpretation = NotApplicable
	test1 = NotApplicable
	test2 = NotApplicable
	Result1 = NotApplicable
	Result2 = NotApplicable
	CategoryCode = NotApplicable
	TemplateName = NotApplicable
	CompanyName = NotApplicable
	key = record.KEY_FIELD
	value = record.Txt
	try:	
		for index, Template_pat in enumerate(Arr_Template_pat):
			if Template_pat.search(value):
				CategoryCode = (Arr_Attr_Template[index])[0]
				TemplateName= (Arr_Attr_Template[index])[1]
				CompanyName=(Arr_Attr_Template[index])[2]
				Patient_Details = get_Patient_Details(value,Arr_Attr_Template[index])
				First_Name = Patient_Details[0]
				Last_Name = Patient_Details[1]
				DOB = Patient_Details[2]
				Gender = Patient_Details[3]
				SpecimenType = Patient_Details[4]
				SpecimenDate = Patient_Details[5]
				ReportDate = Patient_Details[6]
				AccessionDate = Patient_Details[7]
				Interpretation = Patient_Details[8]
				test1 = Patient_Details[9]
				test2 = Patient_Details[10]
				Result1 = Patient_Details[11]
				Result2 = Patient_Details[12]
	except:
		sys.stderr.write("Error occurred while preparing Inter_cat data")
	try:
		tmp_list.append(key)
		tmp_list.append(First_Name)
		tmp_list.append(Last_Name)
		tmp_list.append(DOB)
		tmp_list.append(Gender)
		tmp_list.append(SpecimenType)
		tmp_list.append(SpecimenDate)
		tmp_list.append(ReportDate)
		tmp_list.append(AccessionDate)
		tmp_list.append(Interpretation)
		tmp_list.append(test1)
		tmp_list.append(test2)
		tmp_list.append(Result1)
		tmp_list.append(Result2)
		tmp_list.append(CategoryCode)
		tmp_list.append(TemplateName)
		tmp_list.append(CompanyName)
	except:
		sys.stderr.write("Error occurred while preparing tmp_list data")
	return tmp_list

def prepare_data_hbase(record):
	try:
		key=str(record[0])
		FirstName=str(record[1])
		LastName=str(record[2])
		DOB=str(record[3])
		Gender=str(record[4])
		SpecimenType=str(record[5])
		SpecimenDate=str(record[6])
		ReportDate=str(record[7])
		AccessionDate=str(record[8])
		Interpretation=str(record[9])
		test1_details=str(record[10])
		test2_details=str(record[11])
		test1_result=str(record[12])
		test2_result=str(record[13])
		CategoryCode=str(record[14])
		TemplateName=str(record[15])
		CompanyName=str(record[16])
		key_spl=key.split("|")
		PatId=str(key_spl[0])
		PracId=str(key_spl[1])
		DocName=str(key_spl[2])
		data=((key,[key,"Pat","Patient_ID",PatId]),
			(key,[key,"Pat","Practice_ID",PracId]),
			(key,[key,"Doc","Document_Name",DocName]),
			(key,[key,"Pat","First_Name",FirstName]),
			(key,[key,"Pat","Last_Name",LastName]),
			(key,[key,"Pat","DOB",DOB]),
			(key,[key,"Pat","Gender",Gender]),
			(key,[key,"Doc","Sample_Type",SpecimenType]),
			(key,[key,"Doc","Sample_Draw_Date",SpecimenDate]),
			(key,[key,"Doc","Report_Date",ReportDate]),
			(key,[key,"Doc","Sample_Accession_Date",AccessionDate]),
			(key,[key,"Doc","Interpetation",Interpretation]),
			(key,[key,"Doc","Test1",test1_details]),
			(key,[key,"Doc","Test2",test2_details]),
			(key,[key,"Doc","Result1",test1_result]),
			(key,[key,"Doc","Result2",test2_result]),
			(key,[key,"Doc","Category_Code",CategoryCode]),
			(key,[key,"Doc","Template_Name",TemplateName]),
			(key,[key,"Doc","Companyr_Name",CompanyName]))
		return data
	except:
		sys.stderr.write("Error occurred while preparing data for HBase")
		return ""

def start_HBASE_download(spark):
	sqlc=SQLContext(spark)
	
	host = 'ddcaxtdna03.mckesson.com,ddcaxtdna01.mckesson.com,ddcaxtdna02.mckesson.com'
	port = '2181'
	table = 'mDNA_Biomarker_Unstructured_NLP_DocLevel'
	parent = '/hbase'
	keyConv = "org.apache.spark.examples.pythonconverters.StringToImmutableBytesWritableConverter"
	valueConv = "org.apache.spark.examples.pythonconverters.StringListToPutConverter"
	conf = {"hbase.zookeeper.quorum": host,
				"zookeeper.znode.parent": "/hbase",
				"hbase.mapred.outputtable": table,
				"mapreduce.outputformat.class": "org.apache.hadoop.hbase.mapreduce.TableOutputFormat",
				"mapreduce.job.output.key.class": "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
				"mapreduce.job.output.value.class": "org.apache.hadoop.io.Writable"}
	
	hbase_df = sqlc.read.format('org.apache.hadoop.hbase.spark')\
		.option('hbase.table','mDNA_Biomarker_Unstructured')\
		.option('hbase.columns.mapping', 		'KEY_FIELD STRING :key, Txt STRING OCR:Text')\
		.option('hbase.use.hbase.context', False).option('hbase.config.resources', 'file:///etc/hbase/conf/hbase-site.xml').load()
	
	hbase_df.registerTempTable("mDNA_Biomarker_ILS")
	
	data_df = sqlc.sql('select * from mDNA_Biomarker_ILS where lower(Txt) LIKE "%brca%"')
	extract_data_rdd = data_df.rdd.map(get_attr_code)
	hbase_data_rdd=extract_data_rdd.flatMap(prepare_data_hbase)
	hbase_data_rdd.saveAsNewAPIHadoopDataset(conf=conf,keyConverter=keyConv,valueConverter=valueConv)
	hbase_data_rdd.saveAsNewAPIHadoopDataset(conf=conf,keyConverter=keyConv,valueConverter=valueConv)
	
if __name__ == "__main__":
    # Init Spark Session
	spark= SparkContext(appName = "HBaseRead")
    ## Call Startup function to initiate the 
	start_HBASE_download(spark)
    ## Process files from NFS directories
    ##start_NFS_download(spark)
    ## Stop the application once it is done
	spark.stop()
