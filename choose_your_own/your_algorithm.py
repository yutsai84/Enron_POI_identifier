#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
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


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

try:
    prettyPicture(neigh, features_test, labels_test)
except NameError:
    pass

try:
    prettyPicture(ada, features_test, labels_test)
except NameError:
    pass

try:
    prettyPicture(ram, features_test, labels_test)
except NameError:
    pass