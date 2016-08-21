#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split =40)
clf = clf.fit(features_train,labels_train)
accu = clf.score(features_test,labels_test)

print "accu_DT",accu
#number = len(features_train[0])
#########################################################
# knn
from sklearn.neighbors import KNeighborsClassifier
neigh=KNeighborsClassifier(n_neighbors=3)
neigh.fit(features_train,labels_train)
accu_KN = neigh.score(features_test,labels_test)

print "accu_KN",accu_KN
# adaboost
from sklearn.ensemble import AdaBoostClassifier
ada=AdaBoostClassifier()
ada.fit(features_train,labels_train)
accu_ada = ada.score(features_test,labels_test)

print "accu_ada",accu_ada
#random forest
from sklearn.ensemble import RandomForestClassifier
ram = RandomForestClassifier()
ram.fit(features_train,labels_train)
accu_ram = ram.score(features_test,labels_test)

print "accu_ram", accu_ram