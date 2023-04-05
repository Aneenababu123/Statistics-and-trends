# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 00:24:49 2023

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt


def read_data(filename):                                                                                                                                                                                                                                                 
    """
    Given dataframe reads the data and returns the pandas objects.
    
    """
    #Reads the data from csv 
    df = pd.read_csv(filename, skiprows=4)
    return df
    #Returns the dataframe


def filter_data(df, col, value, con, yr):
    """
    Given functions read the csv data file,returns the dataframe and transpose the dataframes.
    
    
    """
    #Grouping the datas with it's column value 
    da1 = df.groupby(col, group_keys=True)
    #Retrives the data
    da1 = da1.get_group(value)
    #Resetting the data
    da1 = da1.reset_index()
    #Setting the country name as the new index of the data1
    da1.set_index('Country Name', inplace=True)
    #Sorting the data from dataframe
    da1 = da1.loc[:, yr]
    da1 = da1.loc[con, :]
    #Dropping the NAN values from dataframe
    da1 = da1.dropna(axis=1)
    #Resetting the index
    da1 = da1.reset_index()
    #Transposing the index 
    da2 = da1.set_index('Country Name')
    da2 = da2.transpose()
    #returning the dataframe for the heat map
    return da1, da2

def plot1(data, title, x, y):
    """Function for bar plot"""
    
    #Reading data the from for dataframe
    ax = data.plot.bar(x='Country Name', rot=0, figsize=(50, 30), fontsize=50)
    #Sets the location for y axis
    ax.set_yticks([0, 20, 40, 60, 80])
    #Set the title for plot
    ax.set_title(title, fontsize=50)
    #Set label for x axis
    ax.set_xlabel(x, fontsize=50)
    #Set label for y label
    ax.set_ylabel(y, fontsize=50)
    ax.legend(fontsize=50)
    #Save the bar plot as png
    plt.savefig(title + '.png')
    plt.show()
    return

#Country1 used for the data analysis
country1 = ['India', 'Pakistan', 'Peru', 'Afghanistan']
#years used for the data analysis
year = ['2000', '2003', '2004', '2006', '2008', '2010']
#Reads data from csv file
data = read_data("Environment.csv")
da2, da3 = filter_data(
    data, 'Indicator Name', 'CO2 emissions from solid fuel consumption (% of total)', country1, year)
#Print the data
print(da2)
print(da3)
#Calling the bar plot function.
plot1(da2, 'C02 emissions', 'Countries', 'C02 emissions')

da4, da5 = filter_data(
    data, 'Indicator Name', 'CO2 emissions from liquid fuel consumption (% of total)', country1, year)
print(da4)
print(da5)
#Calling the bar plot function.
plot1(da4, 'CO2 Emissions', 'Countries', 'C02 Emissions')

