#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

# load enron data
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# size of data set
print "enron data set size: ", len(enron_data.keys())

# features per person
print "enron data features per person:", len(enron_data[enron_data.keys()[0]])

# number of poi
poi = 0
for p in enron_data.keys():
    if enron_data[p]["poi"] == 1:
        poi += 1
print "enron data number of POI:", poi

# total value of stock for James Prentice 
name = "Prentice James".upper()
print "total stock value of %s:" % name, enron_data[name]["total_stock_value"]

# num email messages to POI's from Wesley Colwell
name = "Colwell Wesley".upper()
print "total email messages to POIs from %s:" % name, enron_data[name]["from_this_person_to_poi"]

# value of stock options for Jeffrey K Skilling
name = "Skilling Jeffrey K".upper()
print "value of stock options of %s:" % name, enron_data[name]["exercised_stock_options"]

# num of people with quantifiable salary
num_salaries = 0
for p in enron_data.keys():
    if enron_data[p]["salary"] != None and enron_data[p]["salary"] != "NaN":
        num_salaries += 1
print "total quantifiable salaries:", num_salaries

# num of people with email addresses
num_emails = 0
for p in enron_data.keys():
    if enron_data[p]["email_address"] != None and enron_data[p]["email_address"] != "NaN":
        num_emails += 1
print "total email addresses:", num_emails

# num of people with NaN for their total payments
num_nan_total_payments = 0
for p in enron_data.keys():
    if enron_data[p]["total_payments"] == "NaN":
        num_nan_total_payments += 1
print "total number of people with missing total payments:", num_nan_total_payments