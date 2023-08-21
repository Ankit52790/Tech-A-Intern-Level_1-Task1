# -*- coding: utf-8 -*-
"""Tech-A-Intern:Level_1-Task1:-Iris_Flower_Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UiFqGd5YoDwaY3Fl0a2iHqtXEvvWQI0B

## 1.IRIS FLOWER CLASSIFICATION

```
Iris flower has three species; setosa, versicolor, and virginica, which differs according to their measurements. Now assume that you have the measurements of the iris flowers according to their species, and here your task is to train a machine learning model that can learn from the measurements of the iris species and classify them.
Although the Scikit-learn library provides a dataset for iris flower classification, you can also download the same dataset from here for the task of iris flower classification with Machine Learning.
```

#About Dataset

```
The Iris dataset was used in R.A. Fisher's classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the UCI Machine Learning Repository.
It includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.
The columns in this dataset are:
* Id
* SepalLengthCm
* SepalWidthCm
* PetalLengthCm
* PetalWidthCm
* Species
```

# 2.Importing Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



"""# 3.Importing Dataset"""

#Load the data
df = pd.read_csv('/content/Iris Flower - Iris.csv')

df.head()

df.describe()

"""# 4.Visualization of our Dataset"""

plt.boxplot(df['SepalLengthCm'])

#Visualize the whole dataset
sns.pairplot(df, hue='Species')

sns.heatmap(df.corr())



"""# 5.Data Preparation"""

df.drop('Id',axis=1,inplace=True)

sp={'Iris-setosa':1,'Iris-versicolor':2,'Iris-virginica':3}

df.Species=[sp[i] for i in df.Species]

df



"""# 6.Seperating Input And The Testing"""

#Seperate features  and target
data = df.values

X = data[:,0:4]
Y = data[:,4]
print(X)

print(Y)

#Split the data to train and test dataset.
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
print(X_train)

print(Y_train)

print(X_test)

print(Y_test)



"""# # 7.Model Building


> Support Vector Machine Learning Algorithm

> Logistic Regression

> Decision Tree Classifier







"""



"""# 7.(ii):Logistic Regression"""

from sklearn.linear_model import LogisticRegression
model_LR=LogisticRegression()
model_LR.fit(X_train,Y_train)

prediction2=model_LR.predict(X_test)

#Calculate the accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,prediction2)*100)
for i in range(len(prediction2)):
  print(Y_test[i],prediction2[i])



"""# 8.Detailed Classification Report"""

from sklearn.metrics import classification_report
print(classification_report(Y_test,prediction2))

X_new =np.array([[3, 2, 1 ,0.2],[4.9, 2.2, 3.8, 1.1],[5.3, 2.5, 4.6, 1.9]])

"""## Prediction of the species from the input"""

#Prediction of the species from the input vector
prediction=model_LR.predict(X_new)

print("Prediction of Species: {}".format(prediction))