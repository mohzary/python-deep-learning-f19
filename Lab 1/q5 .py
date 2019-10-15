#!/usr/bin/env python
# coding: utf-8

# A- Perform exploratory data analysis on the data set (like Handling null values, 
# removing  the  features  not  correlated  to  the  target  class,  encoding  the 
# categorical features, ...) 
# [link text](https://www.kaggle.com/uciml/adult-census-income)

# In[1]:



import pandas as pd
import numpy as np


# In[3]:


iLPDataset = pd.read_csv('indian_liver_patient.csv')


# In[4]:


# Display the top three
iLPDataset.head(3)


# In[5]:


iLPDataset.shape


# ## To Handle Null Values

# In[6]:


# Displaying the datatype about the features.
iLPDataset.info()


# In[7]:


#First we get all the numeric features that we need to train our model
# iLPDatasetNumeric = iLPDataset.select_dtypes(include=[np.number])
# iLPDatasetNumeric.info()


# In[8]:


# To Show number of null values in each column in indian_liver_patient dataset 
iLPDatasetNulls = pd.DataFrame(iLPDataset.isnull().sum().sort_values(ascending=False))
iLPDatasetNulls.columns = ['NO# of null values']
iLPDatasetNulls.index.name = 'Feature'
print(iLPDatasetNulls)


# In[9]:


# Remoing null values in Albumin_and_Globulin_Ratio
iLPDataset.Albumin_and_Globulin_Ratio.fillna(iLPDataset.Albumin_and_Globulin_Ratio.mean(),inplace=True)


# In[17]:


# To Show the number of null values again to see if they are gone 
iLPDatasetNulls = pd.DataFrame(iLPDataset.isnull().sum().sort_values(ascending=False)[:25])
iLPDatasetNulls.columns = ['Null Values Count']
iLPDatasetNulls.index.name = 'Feature'
print(iLPDatasetNulls)


# In[18]:


# Get the x_train ready for the use without Gender because we do not need it.
iLP_train = iLPDataset.drop("Gender", axis=1)


# In[19]:


# Performing the scaling to get all the values at the same level
from sklearn import preprocessing
iLPscaler = preprocessing.StandardScaler()
iLPscaler.fit(iLP_train)
iLPX_scaled_array = iLPscaler.transform(iLP_train)
iLPX_scaled_train = pd.DataFrame(iLPX_scaled_array, columns = iLP_train.columns)
iLPX_scaled_train.head(5)


# In[21]:


# to get y_train ready for the training
iLP_y = iLPX_scaled_train["Dataset"].values
iLP_y = iLP_y.astype('int')


# In[23]:


from sklearn.model_selection import train_test_split
# split the dataset into train and test data
X_train, X_test, y_train, y_test = train_test_split(iLPX_scaled_train, iLP_y, test_size=0.20, random_state=0, stratify=iLP_y)


# # Naive Bayes

# In[24]:


from sklearn.naive_bayes import GaussianNB
# Creating Naive Bayes object for the classification
NaBa = GaussianNB()


# In[25]:


# For starting the train
NaBaResult = NaBa.fit(X_train, y_train)


# In[26]:


iLPpred = NaBa.predict(X_test) 
round(NaBaResult.score(X_test, y_test) * 100, 2)


# # Support Vector Machines(SVM)

# In[27]:


from sklearn.svm import SVC

# Creating Support Vector Machines object for the classification
iLPsvc = SVC(kernel='linear')
# Here where the training starts
SVCResult = iLPsvc.fit(X_train, y_train)

SVMiLPpred = SVCResult.predict(X_test)
round(SVCResult.score(X_test, y_test) * 100, 2)


# # K-nearest neighbors

# In[28]:


from sklearn.neighbors import KNeighborsClassifier
# Creating the K nearest neighbors object for the classification
iLPKNN = KNeighborsClassifier(n_neighbors=3)
# To train the model
KNNResult = iLPKNN.fit(X_train,y_train)

KNNiLPpred = iLPKNN.predict(X_test) 
round(KNNResult.score(X_test, y_test) * 100, 2)


# In[ ]:




