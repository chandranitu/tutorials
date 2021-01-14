# GDP Creation and prediction

#First column = year,
#Second column — GDP 
#Third column — Number of vehicles sold. 

import pandas
from sklearn.svm import SVC
import csv
import numpy
import os


# Load dataset Direct
#url=sc.textFile('hdfs://ml/sample.txt')

#file = open("sample.txt","w") 
#data = open("/home/hadoop/hadoop/hadoop_working/DataScience/ML/Supervised/Regression/code/sample.txt","r")

filename = 'gdp.txt'
raw_data = open(filename, 'rt')
names = ['year', 'GDP', 'Vehicle']
dataset = pandas.read_csv(filename, names=names)
#shape
print(dataset.shape)
#head
print(dataset.head(20))
# descriptions
print(dataset.describe())


def read_data():data = open("sample.txt","r") gdp_sale = collections.OrderedDict()
for line in data.readlines()[1:]:record = line.split(",")
gdp_sale[float(record[1])] = float(record[2].replace('\n', ""))
return gdp_sale

def step_cost_function_for(gdp_sale, constant, slope) :global stepSize
    diff_sum_constant = 0 # diff of sum for constant 'c' in "c + ax" equation
    diff_sum_slope = 0  # diff of sum for 'a' in "c + ax" equation
    gdp_for_years = list(gdp_sale.keys())

    for year_gdp in gdp_for_years: # for each year's gdp in the sample data
        # get the sale for given 'c' and 'a'by giving the GDP for this sample record
        trg_data_sale = sale_for_data(constant, slope, year_gdp) # calculated sale for current 'c' and 'a'
        a_year_sale = gdp_sale.get(year_gdp) # real sale for this record
        diff_sum_slope = diff_sum_slope + ((trg_data_sale - a_year_sale) * year_gdp) # slope's (h(y) - y) * x
        diff_sum_constant = diff_sum_constant + (trg_data_sale - a_year_sale) # consant's (h(y) - y)

    step_for_constant = (stepSize / len(gdp_sale)) * diff_sum_constant # distance to be moved by c
    step_for_slope = (stepSize / len(gdp_sale)) * diff_sum_slope # distance to be moved by a
    new_constant = constant - step_for_constant # new c
    new_slope = slope - step_for_slope # new a
    return new_constant, new_slope

#    Function to get the sales of vehicles provided the values of c, a and x. Used by above function for each sample data (gdp).

def sale_for_data(constant, slope, data):
    return constant + slope * data   # y = c + ax format

#    Iteration to get optimum weights ie optimum values of c and a. It will stop if c and a both are not moving more than 0.01 in next iteration.

def get_weights(gdp_sale) :
    constant = 1
    slope = 1
    accepted_diff = 0.01

    while 1 == 1:  # continue till we reach local minimum
        new_constant, new_slope = step_cost_function_for(gdp_sale, constant, slope)
        # if the diff is too less then lets break
        if (abs(constant - new_constant) <= accepted_diff) and (abs(slope - new_slope) <= accepted_diff):
            print "done. Diff is less than " + str(accepted_diff)
            return new_constant, new_slope
        else:
            constant = new_constant
            slope = new_slope
            print "new values for constant and slope are " + str(new_constant) + ", " + \
                  str(new_slope)

 #   And of course the main function

def main() :
    contant, slope = get_weights(read_data())
    print "constant :" + contant + ", slope:" + slope

if __name__ == '__main__':
    main()

#y (vehicles sales) = 1.43 + 3.84 * x  
#    x is value of GDP

#So if we have GDP as 7.5 this year then we will have passenger vehicles sales next year as — 1.43 7.5*3.84 = 30.23
Full program

#The complete program is below. Its also on github at https://github.com/skhurana333/ml/blob/master/linearRegSingleVariant.py

# sales of vehicle as a function of GDP (for India)

import collections

stepSize = 0.01

def read_data() :
    data = open("vehicle_sale_data" , "r")
    gdp_sale = collections.OrderedDict()
    for line in data.readlines()[1:] :
        record = line.split(",")
        gdp_sale[float(record[1])] = float(record[2].replace('\n', ""))

    return gdp_sale

def sale_for_data(constant, slope, data):
    return constant + slope * data   # y = c + ax format

def step_cost_function_for(gdp_sale, constant, slope) :
    global stepSize
    diff_sum_constant = 0 # diff of sum for constant 'c' in "c + ax" equation
    diff_sum_slope = 0  # diff of sum for 'a' in "c + ax" equation
    gdp_for_years = list(gdp_sale.keys())

    for year_gdp in gdp_for_years: # for each year's gdp in the sample data
        # get the sale for given 'c' and 'a'by giving the GDP for this sample record
        trg_data_sale = sale_for_data(constant, slope, year_gdp) # calculated sale for current 'c' and 'a'
        a_year_sale = gdp_sale.get(year_gdp) # real sale for this record
        diff_sum_slope = diff_sum_slope + ((trg_data_sale - a_year_sale) * year_gdp) # slope's (h(y) - y) * x
        diff_sum_constant = diff_sum_constant + (trg_data_sale - a_year_sale) # consant's (h(y) - y)

    step_for_constant = (stepSize / len(gdp_sale)) * diff_sum_constant # distance to be moved by c
    step_for_slope = (stepSize / len(gdp_sale)) * diff_sum_slope # distance to be moved by a
    new_constant = constant - step_for_constant # new c
    new_slope = slope - step_for_slope # new a

    return new_constant, new_slope

def get_weights(gdp_sale) :
    constant = 1
    slope = 1
    accepted_diff = 0.01

    while 1 == 1:  # continue till we reach local minimum
        new_constant, new_slope = step_cost_function_for(gdp_sale, constant, slope)
        # if the diff is too less then lets break
        if (abs(constant - new_constant) <= accepted_diff) and (abs(slope - new_slope) <= accepted_diff):
            print "done. Diff is less than " + str(accepted_diff)
            return new_constant, new_slope
        else:
            constant = new_constant
            slope = new_slope
            print "new values for constant and slope are " + str(new_constant) + ", " + \
                  str(new_slope)

def main() :
    contant, slope = get_weights(read_data())
    print "constant :" + contant + ", slope:" + slope

if __name__ == '__main__':
    main()

   
