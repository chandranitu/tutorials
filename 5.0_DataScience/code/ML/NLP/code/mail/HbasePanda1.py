
import time
import signal
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

Cat1_regex1 = '(?:.+Interpretation)(.+)(?:nTest.+)'
Cat1_regex2 = r'[^A-Z ]+'
Cat1_regex3 = r'(?:Result Interpretationn)(.+)(?:nAnalysis)'
Cat1_regex4 = r'(.+)(?:nBRCO?A[1-2]?Z?) | (.+)'
Cat1_regex5 = r'(^B.+ing)|(?:.+ed(?:\s\S+)?n)((?:\S+\s\S+){2})(?:)'
Cat1_regex6 = r'(?:\S+\s\S+\s)((\S+\s\S+){2})(?:\s.+)'
Cat1_regex7 = r'(?:n)(BRC.+)'
Cat1_regex8 = r'(^B.+ing)|(?:.+ed(?:\s\S+)?n)((?:\S+\s\S+){2}?)(?:)'
Cat_regex1 = '[\n+]'
Cat_regex2 = r'[^A-Z ]+'

Cat2_regex1 = r'\Interpretation.*\n.*\n'
Cat2_regex2 = 'Interpretation'
Cat2_regex3 = r'(?:n?\s?(?:.+-\s)?)(BRCO?A[1-2]?Z?)(?:.+BRCO?A[1-2]?Z?\s(?:~\s)?)'
Cat2_regex4 = '(?:BRCO?A[1-2]?Z?\s(?:~\s)?)(\w+(?:\s\w+)?)(?:(?:\s\S)?nBRC)'
Cat2_regex5 = r'(?:BRCO?A[1-2]?Z?.+n)(BRCO?A[1-2]?Z?)(?:\s)'
Cat2_regex6 = '(?:BRCO?A[1-2]?Z?\s(?:~\s)?)(\w+(?:\s\w+)?)(?:n(?:\.\s)?Interpretationn)'

Cat3_regex1 = r'\RESULT:.{1,80}'
Cat3_regex2 = 'RESULT:'
Cat3_regex3 = '(?:.+ADDITIONAL FINDINGS:\s)(.+)(?:nDetails\s.+)'


Arr_Template_regex=[]
#Arr_Template_regex.append(r'Genetic\sTest\sResult')
Arr_Template_regex.append(r'Genetic Test Result')
Arr_Template_regex.append(r'myRisk Genetic Result')
Arr_Template_regex.append(r'BRCA1 and BRCA2 Analysis Result')
Arr_Template_regex.append(r'BRCA1 and BRCAZ Analysis Result')
Arr_Template_regex.append(r'Large Rearrangement Analysis Result')
Arr_Template_regex.append(r'Three Mutation BRCA1')
Arr_Template_regex.append(r'Gene Sequence Result')
Arr_Template_regex.append(r'6 High-Risk Hereditary')
Arr_Template_regex.append(r'17 Genes Associated')
Arr_Template_regex.append(r'28 Genes Associated')
Arr_Template_regex.append(r'23 Genes Associated')
Arr_Template_regex.append(r'24 Genes Associated')
Arr_Template_regex.append(r'Oncology Genetic Test Report')
Arr_Template_regex.append(r'Comprehensive BRCA1/2 Analysis')
Arr_Template_regex.append(r'Myriad Accession Number')
Arr_Template_regex.append(r'Gene-Specific BRACAnalysis')
Arr_Template_regex.append(r'Single Site Analysis Result')
Arr_Template_regex.append(r'Invitae')
Arr_Template_regex.append(r'BRCAT and BRCA2Z Analysis Result')

Arr_Attr_Template=[]
# Attr_Templatex - Array of 
#	Category
#	Template_Name
#	Company_Name

Arr_Attr_Template.append(['Category3','Genetic Test Result','Myriad myRisk'])
Arr_Attr_Template.append(['Category3','myRisk Genetic Result','Myriad myRisk'])
Arr_Attr_Template.append(['Category1','BRACAnalysis CDx FDA Approved BRCA1 and BRCA2 Analysis Result','Myriad'])
Arr_Attr_Template.append(['Category1','BRACAnalysis CDx FDA Approved BRCA1 and BRCA2 Analysis Result','Myriad']) # There will be removed after OCR Text quality improvement with the help of fuzzy match.
Arr_Attr_Template.append(['Category1','BRACAnalysis Rearrangement Test Full Gene BRCA1-BRCA2 Large Rearrangement Analysis Result','Myriad'])
Arr_Attr_Template.append(['Category1','Multisite 3 BRACAnalysis Three Mutation BRCA1 and BRCA2 Analysis for Ashkenazi Individuals','Myriad'])
Arr_Attr_Template.append(['Category2','BRACAnalysis Comprehensive BRCA1-BRCA2 Gene Sequence Result','Myriad'])
Arr_Attr_Template.append(['Category4','BRCAplus: Analyses of 6 High-Risk Hereditary Breast Cancer Genes','Ambry Genetics'])
Arr_Attr_Template.append(['Category4','BreastNext: Anlyses of 17 Genes Associated with Hereditary Breast Cancer','Ambry Genetics'])
Arr_Attr_Template.append(['Category4','CancerNext: Analyses of 28 Genes Associated with Hereditary Cancer','Ambry Genetics'])
Arr_Attr_Template.append(['Category4','OvaNext: Analyses of 23 Genes Associated with Hereditary Ovarian Cancer','Ambry Genetics'])
Arr_Attr_Template.append(['Category4','OvaNext: Analyses of 24 Genes Associated with Hereditary Ovarian Cancer','Ambry Genetics'])
Arr_Attr_Template.append(['Category5','Oncology Genetic Test Report','Gene Dx'])
Arr_Attr_Template.append(['Category6','Comprehensive BRCA1/2 Analysis','Integrated Genetics'])
Arr_Attr_Template.append(['Category7','BRACAnalysis Genetic Variant of Uncertain Clinical Significance','Myriad'])
Arr_Attr_Template.append(['Category1','Gene-Specific BRACAnalysis BRCA1 Analysis Result','Myriad'])
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


Cat_pat1 = re.compile(Cat_regex1)
Cat_pat2 = re.compile(Cat_regex2)


Category1_pat1 = re.compile(Cat1_regex1)
Category1_pat2 = re.compile(Cat1_regex2)
Category1_pat3 = re.compile(Cat1_regex3)
Category1_pat4 = re.compile(Cat1_regex4)
Category1_pat5 = re.compile(Cat1_regex5)
Category1_pat6 = re.compile(Cat1_regex6)
Category1_pat7 = re.compile(Cat1_regex7)
Category1_pat8 = re.compile(Cat1_regex8)

Category2_pat1 = re.compile(Cat2_regex1)
Category2_pat2 = re.compile(Cat2_regex2)
Category2_pat3 = re.compile(Cat2_regex3)
Category2_pat4 = re.compile(Cat2_regex4)
Category2_pat5 = re.compile(Cat2_regex5)
Category2_pat6 = re.compile(Cat2_regex6)

Category3_pat1 = re.compile(Cat3_regex1)
Category3_pat2 = re.compile(Cat3_regex2)
Category3_pat3 = re.compile(Cat3_regex3)


Arr_Template_pat=[]
#for index, Template_regex in enumerate(Arr_Template_regex):
for Template_regex in Arr_Template_regex:
	Template_pat=re.compile(Template_regex)
	Arr_Template_pat.append(Template_pat)


# To extract Category1 Test1 and Test result1 from OCR Text
def get_test1_cat1(all_lines):
	Cat_details1=[]
	test1_details="Notfound"
	test1_result="Notfound"
	tc1 = Category1_pat3.search(all_lines)
	try:
		tc2 = Category1_pat4.search(tc1.group(1))
		tc3 = Category1_pat5.search(tc2.group(1))
		test1_details = tc3.group(1)
		tc4 = Category1_pat6.search(tc2.group(1))
		test1_result = tc4.group(1)
	except:
		test1_result = "Notfound"
		test1_details = "Notfound"
	try:
		Cat_details1.append(test1_details)
		Cat_details1.append(test1_result)
		print (Cat_details1)
		return Cat_details1
	except:
		sys.stderr.write("Error occurred while preparing test1 cat1 data")
		print (Cat_details1)
		return Cat_details1

# To extract Category1 Test2 and Test result2 from OCR Text
def get_test2_cat1(all_lines):
	test2_details="Notfound"
	test2_result="Notfound"
	Cat_details2=[]
	tc1 = Category1_pat3.search(all_lines)
	try:
		tc2 = Category1_pat7.search(tc1.group(1))
		tc3 = Category1_pat8.search(tc2.group(1))
		test2_details = tc3.group(1)
		tc4 = Category1_pat6.search(tc2.group(1))
		test2_result = tc4.group(1)
	except:
		test2_result = "Notfound"
		test2_details = "Notfound"
	try:
		Cat_details2.append(test2_details)
		Cat_details2.append(test2_result)
		print (Cat_details2)
		return Cat_details2
	except:
		print (Cat_details2)
		sys.stderr.write("Error occurred while preparing test2 cat1 data")
		return Cat_details2

# To extract Category2 Test1 and Test result1 from OCR Text
def get_test1_cat2(all_lines):
	Cat_details1=[]
	test1_details="Notfound"
	test1_result="Notfound"
	tc1 = Category2_pat3.search(all_lines)
	try:
		test1_details = tc1.group(1)
	except:
		test1_details = "Notfound"
	tc2 = Category2_pat4.search(all_lines)
	try:
		test1_result = tc2.group(1)
	except:
		test1_result = "Notfound"
	try:
		Cat_details1.append(test1_details)
		Cat_details1.append(test1_result)
		print (Cat_details1)
		return Cat_details1
	except:
	print (Cat_details1)
		sys.stderr.write("Error occurred while preparing test1 cat2 data")
		return Cat_details1

# To extract Category2 Test2 and Test result2 from OCR Text
def get_test2_cat2(all_lines):
	test2_details="Notfound"
	test2_result="Notfound"
	Cat_details2=[]
	tc1 = Category2_pat5.search(all_lines)
	try:
		test2_details = tc1.group(1)
	except:
		test2_details = "Notfound"
		
	tc2 = Category2_pat6.search(all_lines)
	try:
		test2_result = tc2.group(1)
	except:
		test2_result = "Notfound"
	try:
		Cat_details2.append(test2_details)
		Cat_details2.append(test2_result)
		print (Cat_details2)
		return Cat_details2
	except:
	print (Cat_details2)
		sys.stderr.write("Error occurred while preparing cat 2 test2 data")
		return Cat_details2

# To extract Category3 Test1 and Test result1 from OCR Text
def get_test1_cat3(all_lines):
	Cat_details1=[]
	test1_details="Notfound"
	test1_result="Notfound"
	tc1 = Category3_pat3.search(all_lines)
	try:
		test1_result = tc1.group(1)
	except:
		test1_result = "Notfound"
	try:
		Cat_details1.append(test1_details)
		Cat_details1.append(test1_result)
		print (Cat_details1)
		return Cat_details1
	except:
		print (Cat_details1)
		sys.stderr.write("Error occurred while preparing test1 data")
		return Cat_details1

# To extract Result of medical report(OCR Text) 
def get_Inter_cat(all_lines,Attr_Template):
	Category_pat1=None
	Category_pat2=None
	test1='Notfound'
	test2='Notfound'
	Result1='Notfound'
	Result2='Notfound'
	ResultCat='Notfound'
	Catdetails=[]
	Cat_details1=[]
	Cat_details2=[]
	
	if Attr_Template[0] == 'Category1':
		Cat_pat1=Category1_pat1
		Cat_pat2=Category1_pat2
		Cat_details1=get_test1_cat1(all_lines)
		Cat_details2=get_test2_cat1(all_lines)
	elif Attr_Template[0] == 'Category2':
		Cat_pat1=Category2_pat1
		Cat_pat2=Category2_pat2
		Cat_details1=get_test1_cat2(all_lines)
		Cat_details2=get_test2_cat2(all_lines)
	elif Attr_Template[0] == 'Category3':
		Cat_pat1=Category3_pat1
		Cat_pat2=Category3_pat2
		Cat_details1=get_test1_cat3(all_lines)
		Cat_details2=['Notfound', 'Notfound']
	IC = Cat_pat1.search(all_lines)
	try:
		ResultCat = str(Cat_pat2.sub(space_l, IC.group(1)))
	except:
		ResultCat='Notfound'
	try:
		test1 = Cat_details1[0]
		test2 = Cat_details2[0]
		Result1 = Cat_details1[1]
		Result2 = Cat_details2[1]
		Catdetails.append(ResultCat)
		Catdetails.append(test1)
		Catdetails.append(test2)
		Catdetails.append(Result1)
		Catdetails.append(Result2)
		return Catdetails
	except:
		sys.stderr.write("Error occurred while preparing Catdetails append data")
		return ''


# To extract attributes the Report(OCR Text) - category number, template name, company name and Interpretation.
def get_attr_code(all_lines):
	attr=[]
	Catdetails = []
	CategoryCode = "NotFound"
	ResultCat = 'NotFound'
	TemplateName='NotFound'
	CompanyName='NotFound'
	test1= "NotFound"
	test2= "NotFound"
	Result1= "NotFound"
	Result2= "NotFound"
	try:
		for index, Template_pat in enumerate(Arr_Template_pat):
			if Template_pat.search(all_lines):
				CategoryCode = (Arr_Attr_Template[index])[0]
				TemplateName= (Arr_Attr_Template[index])[1]
				CompanyName=(Arr_Attr_Template[index])[2]
				Catdetails = get_Inter_cat(all_lines,Arr_Attr_Template[index])
		ResultCat=Catdetails[0]
		test1=Catdetails[1]
		test2=Catdetails[2]
		Result1=Catdetails[3]
		Result2=Catdetails[4]
		attr.append(CategoryCode)
		attr.append(TemplateName)
		attr.append(CompanyName)
		attr.append(ResultCat)
		attr.append(test1)
		attr.append(test2)
		attr.append(Result1)
		attr.append(Result2)
		return attr
		print (attr)
	except:
		sys.stderr.write("Error occurred while preparing attr data")
		print (attr)
		return attr

import pandas as pd
import re		
from py4j.protocol import Py4JJavaError
import datetime
import re, sys, os
df = pd.read_csv("/mnt/hbaseinp/task1/ForPocNLPML.csv")
df2 = df.head(2)
a=df2.ocr.apply(get_attr_code)
