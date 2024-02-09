# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:54:11 2023

@author: waleoniolawale
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



"""
using a def function to read the datasets and returns  two 
dataframes: The first is with years as columns, the other with nations.
"""

def read_data(filename, **others):
    """
    Read climate change data and other indicators from the World Bank database and 
    return both the original dataset and its transpose.
    
    Args:
        filename (str): the name of the World Bank data file to read.
        
        **others: additional arguments to pass to the function as needed.
        
    Returns:
        tuple: a tuple containing the original dataset and its transpose.
    """
    # Reading the csv file containing the climate change dataset  for analysis, with years as the columns.
    world_data = pd.read_csv(filename, skiprows=4) 
    
    # Transposing and cleaning the dataset such that the country names are the columns
    world_data2 = pd.DataFrame.transpose(world_data)
    world_data2=world_data2.drop(['Country Name','Country Code','Indicator Code'])
    world_data2.columns=world_data2.iloc[0]
    world_data2=world_data2.iloc[1:]
    
    return world_data, world_data2


# Reading datasets Climate change for the purpose of analysis
world_data, world_data2 = read_data(r"C:\Users\HP\Documents\msc data sc\ADS\ASSIGNMENT 2\DATA SET\API_19_DS2_en_csv_v2_5361599.csv")
print(world_data)


# For this analysis, we will make do with 4 indicators of choice
indicators=world_data[world_data['Indicator Name'].isin(['Arable land (% of land area)','Urban population',
                                                  'CO2 emissions (kt)','Agricultural land (% of land area)'])]

print(indicators.head())



"""
The dataset appears intricate and challenging to handle. To make it more manageable and conducive to analysis,
we will perform a series of data wrangling tasks.
"""
world_data=pd.DataFrame.transpose(indicators) # Transposing the data
print(world_data)

# Pivot the dataset with country name as columns
world_data.columns=world_data.iloc[0]
print(world_data)


# Some rows are not needed in the data, so we apply the drop function
world_data=world_data.drop(['Country Name','Country Code','Indicator Code'])
print(world_data)




"""
selecting 8 countries accross the continents for analysis purpose. 
"""
# Selecting countries for analysis
countries= world_data[['United States', 'Angola', 'Afghanistan', 'Norway', 'China', 'Germany', 'Nigeria', 'France']]

print(countries)




# some values have been lost, we use the isnull and mean functions to Check for them
countries.isnull().mean()



# using the dropna function to drop all missing values from our datasets
countries.dropna(inplace=True)
countries.head()
countries.index
print(countries)


"""
Combination of the datasets and selecting 8 countries within 7 years for the 
purpose of data analysis and easy accessibility from year 1990 to year 2016
"""
#To create a dataframe for the 8 selected countries on electric power consumption (kWh per capital)
arable=countries.iloc[[2,5,8,11,14,17,20],[2,6,10,14,18,22,26,30]]
arable=arable.apply(pd.to_numeric)# converting the data type to a numeric format
arable.index=pd.to_numeric(arable.index) # converting index values to numeric format
print(arable)


#To create a dataframe for the 8 selected countries on Urban population
urban_pop=countries.iloc[[1,6,10,16,21,23,27],[0,4,8,12,16,20,24,28]]
urban_pop=urban_pop.apply(pd.to_numeric) # converting to dataframe data type to a numeric format
urban_pop.index=pd.to_numeric(urban_pop.index) # converting index values to numeric format
print(urban_pop)


#To create a dataframe for the 8 selected countries on Urban population
co2=countries.iloc[[1,6,10,16,21,23,27],[1,5,9,13,17,21,25,29]]
co2=co2.apply(pd.to_numeric) # converting to dataframe data type to a numeric format
co2.index=pd.to_numeric(co2.index) # converting index values to numeric format
print(co2)




#To create a dataframe for the 8 selected countries on CO2 emissions (kt)
Agric=countries.iloc[[1,4,7,10,13,16,19,22],[3,7,11,15,19,23,27,31]]
Agric=Agric.apply(pd.to_numeric)  # converting to data type to a numeric format
Agric.index=pd.to_numeric(Agric.index) # converting index values to numeric format
print(Agric)




"""
Statistical overview for the urban population across selected countries.
Applying Statistical function for the four selected indicators 
across the 8 selected countries.
"""
#Statistical function for Arable Land 
print(arable.describe())
print(arable.mean()) # checking the mean for arable land
print(arable.median()) # checking the median arable land
print(arable.std()) # checking the arable land standard deviation


#statistical function for urban population
print(urban_pop.describe())
print(urban_pop.mean()) # checking the mean urban population
print(urban_pop.median()) # checking the median urban population
print(urban_pop.std()) # checking the urban population standard deviation



#Statistical function for c02 emission
print(co2.describe())
print(co2.mean()) # checking the mean co2
print(co2.median()) # checking the median co2
print(co2.std()) # checking the co2 standard deviation


#Statistical function for electric consumption 
print(Agric.describe())
print(Agric.mean()) # checking the mean co2
print(Agric.median()) # checking the median co2
print(Agric.std()) # checking the co2 standard deviation


plt.style.available



"""
A grouped bar Plot of urban_population for the 8 Countries within 7 years
from the year 1990 to 2016
"""

plt.figure(figsize=(6, 5))
plt.style.use('default')
urban_pop.T.plot(kind='bar')
plt.title('Urban population Trend for the 8 Countries within 7 years')
plt.xlabel('Countries')
plt.ylabel('Urban population')
plt.savefig('urban_pop_plot.png', dpi=300, bbox_inches='tight', pad_inches=0.2)
plt.show()





"""
line Plot of Agricultural land (% of land area) for the 8 Countries within 7 years
from the year 1990 to 2016
"""

plt.figure(figsize=(10,6))
co2.plot()
plt.title('CO2 emissions (kt) for The 7 countries')
plt.xlabel('Years')
plt.ylabel('CO2 emissions (kt)')
plt.legend(co2.columns, bbox_to_anchor=(1.0, 1))
plt.savefig('CO2 emissions (kt)', dpi=300, bbox_inches='tight', pad_inches=0.2)
plt.show()


# making a scatter plot for comparism between co2 and urban in China 
plt.scatter(co2['China'], urban_pop['China'])
plt.title('Comparism between co2 and urban_pop for China')
plt.xlabel('CO2 emissions (kt) for China')
plt.ylabel('Urban population for China')
plt.savefig('scatter plot for china', dpi=300)
plt.show()
