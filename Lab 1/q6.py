


# To import all required modules to apply K-means on google play store dataset 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tricker
import seaborn as sns
from sklearn.cluster import KMeans
import io
import pylab as pl
#from google.colab import files
# %matplotlib inline

"""##  Import dataset from File
To upload file and open it using pandas. Also, to  know dataset content and get some information about dataset features. In this question, we choose google play store dataset. The source of dataset is Kaggle.com.
"""

# To upload file and open it using pandas 
#playStoreFile = files.upload()

gPSDataset = pd.read_csv('googleplaystore.csv')

# To show the first 5 rows in google play store dataset.
print(gPSDataset.head(5))

# To show range of data, number of columns, type of features, and feature names  
print(gPSDataset.info())

"""## To Handle Null Values
In this stage we handle null values in google play store dataset using two techniques. First we remove null values in rating feature by using fillna() function with the mean value. Seecond, we use dropna() function to remove rows that contain null values in the following features: Current Ver, Android Ver, Content Rating, and Type.
"""

# To Show number of null values in each column in google play store dataset 
gPSDnullValues = pd.DataFrame(gPSDataset.isnull().sum().sort_values(ascending=False))
gPSDnullValues.columns = ['NO# of null values']
gPSDnullValues.index.name = 'Feature'
print(gPSDnullValues)

#To fill null values using mean() function, we use this method only with Rating feature
gPSDataset.Rating.fillna(gPSDataset.Rating.mean(),inplace=True)

# To Show number of null values in each column in google play store dataset, to check the difference after we apply fillna() on Rating
gPSDnullValues = pd.DataFrame(gPSDataset.isnull().sum().sort_values(ascending=False))
gPSDnullValues.columns = ['NO# of null values']
gPSDnullValues.index.name = 'Feature'
print(gPSDnullValues)

# To use dropna() function to remove the entire rwo if it contains null value.
gPSDataset = gPSDataset.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

# To Show number of null values in each column in google play store dataset, to check the difference after we apply fillna() and dropna() functions on dataset

gPSDnullValues = pd.DataFrame(gPSDataset.isnull().sum().sort_values(ascending=False))
gPSDnullValues.columns = ['NO# of null values']
gPSDnullValues.index.name = 'Feature'
print(gPSDnullValues)

"""## To Find Top 10 App Genres"""

# To Show Top 10 genres based on number of Application in this step we count number of applications in each genre
topGenres = gPSDataset.Genres.value_counts().sort_values(ascending=False)
topGenres.index.name = 'Genres'
print('Total of application by genres')
print(topGenres[:10])

# To visulize the result, we used matplotlib pie figure to show the result.

# We used top 10 genres from previous step as labels 
labels = topGenres.index[0:10]

# We change figure size to 9,9
plt.figure(figsize=(9,9))

# To assign a title to the figure we used Total of application by genres as the figure title
plt.title('Total of application by genres', fontsize = 14, fontweight='bold')

#To display our result we used pie chart and we used topGenres[:10] as the data
plt.pie(topGenres[:10],labels = labels, autopct = '%1.0f%%', textprops={'fontsize': 12})
plt.savefig('Total of application by genres.png')
plt.show()

# As shown in dataset info() the type of reviews and rating features are object so we change them to integer type
gPSDataset['Reviews'] = gPSDataset['Reviews'].astype(int)
gPSDataset['Rating'] = gPSDataset['Rating'].astype(int)

# To check the type of rating and reviews after we change their types to integer
gPSDataset.info()

#To show most 10 popular app genres in google play store in term of genre, reviews, and user ratings:

topGenresRR = gPSDataset[['Genres','Reviews', 'Rating']].groupby(['Genres'], as_index=False).sum().sort_values(by=['Reviews'],ascending=False)
topGenresRR[0:10]

# To show statistic report about reviews feature
Reviews = gPSDataset[['Reviews']].describe()
Reviews

# To show statistic report about Rating feature
Rating = gPSDataset[['Rating']].describe()
Rating

"""## To create and train the Model"""

# To check which K is the best using the elbow method based on the result we will train our model using the best number of clusters we get

#To get the two features that we are going to use to categorize applications in google play store: 
gPSDataset_X = gPSDataset[['Reviews' , 'Rating']].iloc[: , :].values

# To Keep tracking of the line shape when we used elbow method

distortionsList = []

# To use different number of clusters when we train our model 
for i in range(1, 11):
    
    # To define a new model object we call it kmModel
    kmModel = KMeans(n_clusters=i, random_state=0)

    #To train the model using fet function using gPSDataset_X data set 
    kmModel.fit(gPSDataset_X)

    # To assign the Sum of squared distances of samples to their closest cluster center in each iteration to the distortionsList.
    distortionsList.append(kmModel.inertia_)

# To visualize the result we get in Elbow method 
plt.title('K-Means in Google Play Store Dataset (Elbow Method)', fontsize = 16, fontweight='bold')
plt.plot(range(1, 11), distortionsList, 'c', marker='o', markeredgecolor = 'b')
plt.xlabel('NO# of clusters', fontsize = 14)
plt.ylabel('Sum of squared distances', fontsize = 14)
plt.savefig('Elbow Method K-means.png', bbox_inches = 'tight')
plt.show()

"""## Result of Elbow Method:
As a result, we find out that K = 3 is the best number of clusters. We will train our model using 3 clusters to categorize application into 3 different groups.
"""

# To define a new object of KMeans with 3 clusters
kmModel2 = KMeans(n_clusters=3,init='k-means++')

# To train our model using the new number of clusters which is 3
kmModel2.fit(gPSDataset_X)

#To Evaluate our model we used predict() function the we show the silhouette score
y_predict_kmeans2 = kmModel2.predict(gPSDataset_X)

from sklearn import metrics
kmModel2_score = metrics.silhouette_score(gPSDataset_X, y_predict_kmeans2)
print('The silhouette score of our model is: ', kmModel2_score)

"""## Clusters Visualization
As a result applications in google play store will by divided into 3 groups
"""

# To visualize our result we used scatter figure

plt.figure(figsize=(8,8))

plt.scatter(gPSDataset_X[y_predict_kmeans2 == 0, 0], gPSDataset_X[y_predict_kmeans2 == 0, 1], s = 100, c = 'blue', label = 'Cluster 1')
plt.scatter(gPSDataset_X[y_predict_kmeans2 == 1, 0], gPSDataset_X[y_predict_kmeans2 == 1, 1], s = 100, c = 'red', label = 'Cluster 2')
plt.scatter(gPSDataset_X[y_predict_kmeans2 == 2, 0], gPSDataset_X[y_predict_kmeans2 == 2, 1], s = 100, c = 'green', label = 'Cluster 3')

#o show the centroid of each application group in the figure
plt.scatter(kmModel2.cluster_centers_[:, 0], kmModel2.cluster_centers_[:, 1], s = 100, c = 'black', label = 'Centroids')

# To create labels and title for our figure
plt.title('Clusters of Applications in Google Play Store', fontsize = 16, fontweight='bold')
plt.xlabel('Reviews', fontsize = 14)
plt.ylabel('Rating', fontsize = 14)
plt.legend(fontsize = 14)
plt.savefig('Google Play Store Application clusters.png', bbox_inches = 'tight')
plt.show()