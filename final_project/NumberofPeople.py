
"""
Created on Thu Jul 28 19:22:17 2016

@author: yuchengtsai
"""

#fo = open('../final_project/poi_names.txt','r')
#fr =fo.readlines()
#print len(fr[2:])

#print enron_data.keys()

#print enron_data["PRENTICE JAMES"].keys()

#print enron_data["PRENTICE JAMES"]["total_stock_value"]

#print enron_data["COLWELL WESLEY"].keys()

#print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
#print sorted(enron_data.keys())

#print enron_data['SKILLING JEFFREY K']['total_payments']

#print enron_data['LAY KENNETH L']['total_payments']

#print enron_data['FASTOW ANDREW S']['total_payments']

#print enron_data['FASTOW ANDREW S']['deferral_payments']

#print enron_data.keys()
#count_salary = 0
#count_email = 0
#
#for key in enron_data.keys():
#    if enron_data[key]['salary'] != 'NaN':
#        count_salary +=1
#    if enron_data[key]['email_address'] != 'NaN':
#        count_email +=1
#    
#print count_salary
#print count_email

#count_nan = 0
#
#for key in enron_data.keys():
#    if enron_data[key]['total_payments'] == 'NaN':
#        count_nan +=1
#print float(count_nan)/len(enron_data.keys())
        
#count_nan = 0
#
#for key in enron_data.keys():
#    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True:
#        count_nan +=1
#        
#print float(count_nan)/len(enron_data.keys())

#print len(enron_data.keys())

count_poi =0
for key in enron_data.keys():
    if enron_data[key]['poi'] == True:
        count_poi +=1
        
print count_poi
