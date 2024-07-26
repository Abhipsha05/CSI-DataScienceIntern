#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


# In[3]:


loan_dset = pd.read_csv('A:\csi_assignments\Loan Status Prediction\Training Dataset.csv')


# In[4]:


type(loan_dset)


# In[5]:


loan_dset.head()


# In[6]:


loan_dset.shape 


# In[7]:


loan_dset.describe()


# In[8]:


loan_dset.isnull().sum()


# In[9]:


loan_dset = loan_dset.dropna()


# In[10]:


loan_dset.isnull().sum()


# In[11]:


loan_dset.replace({"Loan_Status":{'N':0, 'Y':1}}, inplace = True)


# In[12]:


loan_dset.head()


# In[13]:


loan_dset['Dependents'].value_counts()


# In[14]:


loan_dset = loan_dset.replace(to_replace = '3+', value=4)


# In[15]:


loan_dset['Dependents'].value_counts()


# In[16]:


sns.countplot(x = 'Education', hue = 'Loan_Status', data=loan_dset)


# In[17]:


sns.countplot(x = 'Married', hue = 'Loan_Status', data=loan_dset)


# In[18]:


#convert categorical to numerical
loan_dset.replace({'Married':{'No':0, 'Yes':1},'Gender':{'Female':0, 'Male':1}, 'Self_Employed':{'No':0, 'Yes':1},
                   'Property_Area':{'Rural':0, 'Semiurban':1, 'Urban':2}, 'Education':{'Not Graduate':0, 'Graduate':1}}, inplace=True)


# In[20]:


loan_dset.head()


# In[21]:


#Separating the data and label
X = loan_dset.drop(columns=['Loan_ID', 'Loan_Status'], axis=1)
Y = loan_dset['Loan_Status']


# In[22]:


print(X)
print(Y)


# In[23]:


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.1,stratify=Y, random_state=2)


# In[24]:


print(X.shape, X_train.shape, X_test.shape)


# ### Support Vector Machine Model

# In[38]:


classifier = svm.SVC(kernel='linear')


# In[39]:


classifier.fit(X_train, Y_train)


# In[37]:


#accuracy test
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)


# In[36]:


print("Training data accuracy:", training_data_accuracy)


# In[ ]:


X_test_prediction = classifier.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print("Testing data accuracy:", testing_data_accuracy)


# In[ ]:




