# To import all required modules to get comparison of the clustering algorithms from scikit-learn web page 
import requests
from bs4 import BeautifulSoup as bs
import os


# use request with get function to fetch the scikit-learn web page content to scikitlearnPage variable
scikitlearnPage = requests.get('https://scikit-learn.org/stable/modules/clustering.html#clustering')

# To parse scikit-learn web page content and assign it to soupObj variable
soupObj = bs(scikitlearnPage.content, "html.parser")

# To create a new text file called clustring to write table content to the text file
comparisonFile = open('clustering.txt','a') 

# An empty string to use later when iterate through table content
line = ''

#To Fetch table with class name 
comparisonTable = soupObj.find('table',{'class': 'colwidths-given'})

# To fetch all rows in the table 
tableRows = comparisonTable.findChildren('tr')

# To I terate through rows and columns and get text contents
for row in tableRows:
  tableColumns = row.find_all(['th','td'])
  for column in tableColumns:
    line += column.text + '  |  '
  line += '\n'
  # to write text conten in the file
  comparisonFile.write(line)
  line = ''
# To Close file after we finish writing
comparisonFile.close()

