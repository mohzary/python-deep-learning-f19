
"""


##Multiple Regression On Video Game Dataset To Predict Sales
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pylab as pl
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
# %matplotlib inline



#To open our dataset file using pandas
vGDataset = pd.read_csv('Video_Games_Sales.csv')

#To Show the first five rows in our dataset
vGDataset.head(5)

# To show some infromation about Features and dataset
vGDataset.info()

"""It Shows that there are 16719 rows and 16 features. There are alot of null values in our dataset. So, next step is to hundle null values.

##Remove Null Values
"""

#First we get all the numeric features that we need to train our model
vGDatasetNumeric = vGDataset.select_dtypes(include=[np.number])
vGDatasetNumeric.info()

vGDatasetNulls = pd.DataFrame(vGDatasetNumeric.isnull().sum().sort_values(ascending=False)[:25])
vGDatasetNulls.columns = ['Null Values Count']
vGDatasetNulls.index.name = 'Feature'
print(vGDatasetNulls)

#To remove year of release feature since we do not need it in our training dataset
vGDatasetNumeric = vGDatasetNumeric.drop('Year_of_Release',axis=1)
vGDatasetNumeric.info()

#To remove null values from the following features we used fillna() function to fill the null values with mean values
vGDatasetNumeric.User_Count.fillna(vGDatasetNumeric.User_Count.mean(),inplace=True)
vGDatasetNumeric.Critic_Count.fillna(vGDatasetNumeric.Critic_Count.mean(),inplace=True)
vGDatasetNumeric.Critic_Score.fillna(vGDatasetNumeric.Critic_Score.mean(),inplace=True)

#To check if the null values are all filled in by the mean
vGDatasetNulls = pd.DataFrame(vGDatasetNumeric.isnull().sum().sort_values(ascending=False)[:25])
vGDatasetNulls.columns = ['Null Values Count']
vGDatasetNulls.index.name = 'Feature'
print(vGDatasetNulls)

"""##TP find the top correlated features to the target label (Global_Sales)"""

vGDatasetCorr = vGDatasetNumeric.corr()
print(vGDatasetCorr['Global_Sales'].sort_values(ascending=False),'\n')

sns.heatmap(vGDatasetCorr)

#To Show the relation between Global_Sales and and NA Sales
plt.scatter(vGDatasetNumeric.NA_Sales, vGDatasetNumeric.Global_Sales, color='blue')
plt.xlabel('NA Sales')
plt.ylabel('Global_Sales')
plt.show()

#To Show the relation between Global_Sales and and Critic count
plt.scatter(vGDatasetNumeric.Critic_Count, vGDatasetNumeric.Global_Sales, color='blue')
plt.xlabel('Critic_Count')
plt.ylabel('Global_Sales')
plt.show()

#To Show the relation between Global_Sales and and Critic Score

plt.scatter(vGDatasetNumeric.Critic_Score, vGDatasetNumeric.Global_Sales, color='blue')
plt.xlabel('Critic_Score')
plt.ylabel('Global_Sales')
plt.show()

"""## To Split Data set"""

#To set up the x axis features and target feature

vGDatasetNumeric_X = vGDatasetNumeric.drop('Global_Sales',axis=1)

vGDatasetNumeric_Y = vGDatasetNumeric['Global_Sales']

vGDatasetNumeric_X.head(5)

vGDatasetNumeric_Y.head(5)

#To split the dataset into training and testing datasets
X_train, X_test, Y_train, Y_test = train_test_split(vGDatasetNumeric_X, vGDatasetNumeric_Y, test_size=0.20)

"""##To Create Model"""

#To crate and train our model
vGDMRegr = linear_model.LinearRegression()
vGDModel = vGDMRegr.fit(X_train, Y_train)

"""##Evaluation Metrics and Prediction"""

#To predict
Y_pred = vGDModel.predict(X_test)

#Evaluation Metrics

print('R^2 score:', vGDModel.score(X_test, Y_test))
print ('RMSE is: ', np.sqrt(mean_squared_error(Y_test, Y_pred)))

"""##Result Visualization"""

plt.scatter(Y_pred, Y_test, alpha=.75, color='blue',) 
plt.xlabel('Predicted Value')
plt.ylabel('Actual Value')
plt.title('Video Games Global Sales Prediction Using Multiple Linear Regression Model')
plt.savefig('Video Games Global Sales.png', bbox_inches = 'tight')
plt.show()