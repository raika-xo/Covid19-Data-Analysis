#importing modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
print('Modules imported!')

#importing first dataset
corona_dataset_csv = pd.read_csv('covid19_Confirmed_dataset.csv')

#To print dataset. This will only display first 5 rows. To see more rows enter integer at head.
print(corona_dataset_csv.head())

#Checking No. of (rows,columns) in dataset
print(corona_dataset_csv.shape)

#Cleaning Dataset. Removing columns such as Lat and Long. Incase of deleting row set axis=0 and column axis=1. Inplace replaces data in original dataset.
corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)
print(corona_dataset_csv.head())

#Aggregating the rows by country
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
print(corona_dataset_aggregated.head())

#Shape ( i.e no. of (rows,columns)) of Aggregated dataset
print(corona_dataset_aggregated.shape)

#Visualizing data related to a country. Example : India, China, Italy, Spain. To see legend type plt.legend()
corona_dataset_aggregated.loc["India"].plot()
corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
plt.legend()

#Obtaining plot for first derivative 
corona_dataset_aggregated.loc["India"].diff().plot()

#Find max infection rate for the country
corona_dataset_aggregated.loc["India"].diff().max()

#Find max infection rate for all countries in the form of list
countries = corona_dataset_aggregated.index
max_infection_rate = []
for c in countries:
    max_infection_rate.append(corona_dataset_aggregated.loc[c].diff().max())
    
corona_dataset_aggregated["max_infection_rate"] = max_infection_rate
print(corona_dataset_aggregated.head())
corona_data = pd.DataFrame(corona_dataset_aggregated['max_infection_rate'])

#Adding World Happiness Dataset 
happiness_report_csv = pd.read_csv("worldwide_happiness_report.csv")
print(happiness_report_csv.head())

#Removing unnecessary data
useless_columns = ["Overall rank","Score","Generosity", "Perceptions of corruption"]
happiness_report_csv.drop(useless_columns,axis=1,inplace=True)
print(happiness_report_csv.head())

#Putting name of country as indices of dataset
happiness_report_csv.set_index("Country or region",inplace=True)
print(happiness_report_csv.head())

#Combining the two datasets. No of countries is more in corona_data hence we do inner join in that dataset
data = corona_data.join(happiness_report_csv,how='inner')
print(data.head(10))

#Correlation Matrix
print(data.corr())

#Visualisation of the result 
#Plotting GDP vs Maximum infection rate
x = data["GDP per capita"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y)) #np.log to bring y to scale

#Fitting a curve in above scatterplot
sns.regplot(x,np.log(y))

#Similar plot can be made with other parameters vs Maximum infection rate.
#Conclusion: A positive correlation is obserbed. Hence developed countries are more prone to the virus
#Further Improvement: Correlation can be checked between Death and maximum infection rate to prove the above conclusion true or false.


