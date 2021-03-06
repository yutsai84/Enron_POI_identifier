#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn import cross_validation
features_train,features_test,labels_train,labels_test = cross_validation.train_test_split(features,labels,test_size=0.3,random_state=42)

print "labels_test type:" ,type(labels_test)

### it's all yours from here forward!                                                                   
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf=clf.fit(features_train,labels_train)
accu=clf.score(features_test,labels_test)

print "accu=", accu

# how many POIs 
pred=clf.predict(features_test)
print "pre= ",pred
print "hwo many predicted POIs= ",sum(pred)

import numpy as np
print "labels_test:",np.array([labels_test])
print "no. of POIs in labels_test:",len([e for e in labels_test if e ==1.0])

# how many people total in your test set?
print "no. of people in the test set:",len(labels_test) 

# how many true positive (1 in labels_test and 1 in pred)

count = 0
for i in range(len(labels_test)):
    if labels_test[i] !=1 or pred[i] !=1:
        continue
    if labels_test[i]==pred[i]:
        count +=1

print "no. of trun positive is ",count
#what is the precision?
from sklearn.metrics import *
print "precision",precision_score(labels_test,clf.predict(features_test))
#what is the recall?
print "recall",recall_score(labels_test,clf.predict(features_test))

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

count = 0
for i in range(len(predictions)):
    if predictions[i] !=1 or true_labels[i] !=1:
        continue
    if predictions[i]==true_labels[i]:
        count +=1

print "no. of true positive",count

count = 0
for i in range(len(predictions)):
    if predictions[i] ==1 or true_labels[i] ==1:
        continue
    if predictions[i]==true_labels[i]:
        count +=1

print "no. of true negative ",count

count = 0
for i in range(len(predictions)):
    if predictions[i]==1 and true_labels[i] !=1:
        count +=1

print "no. of false positive",count

count = 0
for i in range(len(predictions)):
    if predictions[i]!=1 and true_labels[i] ==1:
        count +=1

print "no. of false negative",count

print "precision",precision_score(true_labels,predictions)
print "recall",recall_score(true_labels,predictions)
