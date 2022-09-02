# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gT4RIQyL1EcrND8_s_WHiPgKqIneP33D
"""

import pandas as pd
#READ DATASET FROM THE IMAGE
data = {'Features': [1,2,3,6,6,7,10,11],
'Classes': [1,1,2,2,2,1,1,1]}
inputs= [[1,1],[2,1],[3,2],[6,2],[6,2],[7,1],[10,1],[11,1]]
TEMP = pd.DataFrame(inputs, columns=['Features', 'Classes'])
#IMPORT TRAIN TEST SPLITTER FROM SKLEARN PACKAGE
from sklearn.model_selection import train_test_split
#IMPORT KNN ALGORITHM
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
#DIVIDING THE DATASET INTO 2 PARTS THEN TEST_SIZE IS HALF I.E.., 0.5
TRAIN_X, TEST_X, TRAIN_Y, TEST_Y = train_test_split(TEMP.drop('Classes',axis=1),TEMP['Classes'], test_size=0.50,random_state=101)
CLASSIFIER = KNeighborsClassifier(n_neighbors = 3)# AS REQUIRED N=3
CLASSIFIER.fit(TRAIN_X, TRAIN_Y)# FIT THE TRAIN AND TEST DATA
KNeighborsClassifier(n_neighbors=3)
# GET THE PREDICTION
PREDICTION_Y = CLASSIFIER.predict(TEST_X)
#Checking the accuracy score , confusion matrix ,
accuracy = accuracy_score(TEST_Y,PREDICTION_Y)
CONFUSION_MATRIX = confusion_matrix(TEST_Y,PREDICTION_Y)
CONFUSION_MATRIX_DATA_FRAME = pd.DataFrame(CONFUSION_MATRIX, columns = ['Pred -VE', 'Pred +VE'],index = ['Actual -VE', 'Actual +VE'])

#IMPORT TRAIN TEST SPLITTER FROM SKLEARN PACKAGE
from sklearn.model_selection import train_test_split
#IMPORT KNN ALGORITHM
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
#DIVIDING THE DATASET INTO 2 PARTS THEN TEST_SIZE IS HALF I.E.., 0.5
TRAIN_X, TEST_X, TRAIN_Y, TEST_Y = train_test_split(TEMP.drop('Classes',axis=1),TEMP['Classes'], test_size=0.50,random_state=101)
CLASSIFIER = KNeighborsClassifier(n_neighbors = 3)# AS REQUIRED N=3
CLASSIFIER.fit(TRAIN_X, TRAIN_Y)# FIT THE TRAIN AND TEST DATA
KNeighborsClassifier(n_neighbors=3)
# GET THE PREDICTION
PREDICTION_Y = CLASSIFIER.predict(TEST_X)
#Checking the accuracy score , confusion matrix ,
accuracy = accuracy_score(TEST_Y,PREDICTION_Y)
CONFUSION_MATRIX = confusion_matrix(TEST_Y,PREDICTION_Y)
CONFUSION_MATRIX_DATA_FRAME = pd.DataFrame(CONFUSION_MATRIX, columns = ['Pred -VE', 'Pred +VE'],index = ['Actual -VE', 'Actual +VE'])
CONFUSION_MATRIX_DATA_FRAME

TP = CONFUSION_MATRIX[1][1]
TN = CONFUSION_MATRIX[0][0]
FP = CONFUSION_MATRIX[0][1]
FN = CONFUSION_MATRIX[1][0]
CONFUSION_MATRIX_ACCURACY = (float (TP+TN) / float(TP + TN + FP + FN))#ACCURACY
# calculate mis-classification
CONFUSION_MATRIX_MIS_CLASSIFICATION = 1- CONFUSION_MATRIX_ACCURACY#MIS-CLASSIFICAITION
# calculate the sensitivity
CONFUSION_SENSITIVITY = (TP / float(TP + FN))#SENSITIVITY
# calculate the specificity
CONFUSION_SEPCIFICITY = (TN / float(TN + FP))#SPECIFICITY
# calculate precision
CONFUSION_PRECESION = (TN / float(TN + FP))#PRECESION
print('-'*50)
print(f'Accuracy: {round(CONFUSION_MATRIX_ACCURACY,2)}')
print(f'Sensitivity: {round(CONFUSION_SENSITIVITY,2)}')
print(f'Specificity: {round(CONFUSION_SEPCIFICITY,2)}')