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

#########################################################

# declarations
from sklearn.svm import SVC
classifier = SVC(C=10000.0,kernel='rbf')

# cut down data set
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 


# train
t0 = time()
classifier.fit(features_train, labels_train)
print "training time:", round(time() - t0, 3), "s"

# predict
t1 = time()
predict = classifier.predict(features_test)
print "prediction time:", round(time() - t1, 3), "s"

# accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, predict)
print "accuracy:", accuracy

# predict class for 10th element
i = 10
print "class for element %d:" %i, predict[i]

# predict class for 26th element
i = 26
print "class for element %d:" %i, predict[i]

# predict class for 50th element
i = 50
print "class for element %d:" %i, predict[i]

# number of chris (1) emails
print "number of chris(1) emails:", list(predict).count(1)