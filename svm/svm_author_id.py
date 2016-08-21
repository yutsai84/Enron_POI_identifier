#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
clf = SVC(C =10000,kernel='rbf')
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
clf.fit(features_train,labels_train)
accuracy = clf.score(features_test,labels_test)
pred = clf.predict(features_test)
samples = len(pred)
count = 0

for i in range(len(pred)):
    if pred[i]==1:
        count +=1

print count
     
    
#pred_10th = clf.predict(features_test[10])
#pred_26th = clf.predict(features_test[26])
#pred_50th = clf.predict(features_test[50])

print 'accuracy=', accuracy
print 'number of samples=', samples
#print 'pred_10th=', pred_10th
#print 'pred_26th=', pred_26th
#print 'pred_50th=', pred_50th

#########################################################


