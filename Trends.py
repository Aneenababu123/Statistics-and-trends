# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 00:24:49 2023

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


def read_data(filename):                                                                                                                                                                                                                                                 
    """
    Given dataframe reads the data and returns the pandas objects.
    
    """
    #Reads the data from csv 
    df = pd.read_csv(filename, skiprows = 4)
    return df
    #Returns the dataframe


def filter_data(df, col, value, con, yr):
    """
    Given functions read the csv data file,returns the dataframe and transpose the dataframes.
    
    
    """
    #Grouping the datas with it's column value 
    da1 = df.groupby(col, group_keys = True)
    #Retrives the data
    da1 = da1.get_group(value)
    #Resetting the data
    da1 = da1.reset_index()
    #Setting the country name as the new index of the data1
    da1.set_index('Country Name', inplace = True)
    #Sorting the data from dataframe
    da1 = da1.loc[:, yr]
    da1 = da1.loc[con, :]
    #Dropping the NAN values from dataframe
    da1 = da1.dropna(axis = 1)
    #Resetting the index
    da1 = da1.reset_index()
    #Transposing the index 
    da2 = da1.set_index('Country Name')
    da2 = da2.transpose()
    #returning the dataframe for the heat map
    return da1, da2

def stat_data(df, col, value, yr, a):
    """
    Reads a dataframe with different indicator and returns dataframe.
    """
    #Grouping the rows by column values
    df3 = df.groupby(col, group_keys = True)
    #Retriving the data
    df3 = df3.get_group(value)
    #Reset the datas of the dataframe
    df3 = df3.reset_index()
    df2 = df3.set_index('Indicator Name', inplace = True)
    df3 = df3.loc[:, yr]
    #Transposing the index
    df3 = df3.transpose()
    df3 = df3.loc[:,a ]
    #Returns the dataframe for Heat map
    return df3

def plot1(data, title, x, y):
    """Function for bar plot"""
    
    #Reading data the from for dataframe
    ax = data.plot.bar(x='Country Name', rot = 0, figsize = (50, 30), fontsize = 50)
    #Sets the location for y axis
    ax.set_yticks([0, 20, 40, 60, 80])
    #Set the title for plot
    ax.set_title(title, fontsize = 50)
    #Set label for x axis
    ax.set_xlabel(x, fontsize = 50)
    #Set label for y label
    ax.set_ylabel(y, fontsize = 50)
    ax.legend(fontsize=50)
    #Save the bar plot as png
    plt.savefig(title + '.png')
    plt.show()
    return

def plot2(data, title, x, y):
    """Function for line plot"""
    
    #Reading data the from for dataframe
    ax = data.plot.line(figsize = (50, 30), fontsize = 50, linewidth = 6.0)
    #Sets the location for y axis
    ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
    #Set the title for plot
    ax.set_title(title, fontsize = 50)
    #Set label for x axis
    ax.set_xlabel(x, fontsize = 50)
    #Set label for y axis
    ax.set_ylabel(y, fontsize = 50)
    ax.legend(fontsize = 50)
    #Save the bar plot as png
    plt.savefig(title + '.png')
    plt.show()
    return


def heat_map(data):
    """
    The below function visualizes the corelation between multiple indicators.

    """
    plt.figure(figsize = (70,58))
    #Set title
    plt.title("Brazil's Heat map", size=50)
    plt.xticks(rotation=90,horizontalalignment = "center",fontsize = 50)
    plt.yticks(fontsize = 50)
    sns.heatmap(data.corr(),annot = True,annot_kws = {"size":42})
    #Saves heat map as png
    plt.savefig('Brazil_heatmap.png',dpi=150, bbox_inches ='tight')
    plt.show()
    return data



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
plot1(da2, 'CO2 emissions', 'Countries', 'CO2 emissions')

da4, da5 = filter_data(
    data, 'Indicator Name', 'CO2 emissions from liquid fuel consumption (% of total)', country1, year)
print(da4)
print(da5)
#Calling the bar plot function.
plot1(da4, 'CO2 Emissions', 'Countries', 'C02 Emissions')

#Create year and country for line plot
country2 = ['Sri Lanka', 'Myanmar', 'Pakistan', 'Japan', 'Nigeria']
year2 = ['2010', '2013', '2015', '2017', '2019']
da6, da7 = filter_data(
    data, 'Indicator Name', 'Renewable energy consumption (% of total final energy consumption)', country2, year2)
#Print data
print(da6)
print(da7)

#Calling line plot function
plot2(da7, 'Renewable energy consumption', 'Year',
          'Percentage of renewable energy consumption')

da8, da9 = filter_data(
    data, 'Indicator Name', 'Renewable electricity output (% of total electricity output)', country2, year2)
print(da8)
print(da9)
#Calling line plot function
plot2(da9, 'Renewable electricity output', 'Year',
          'Percentage of renewable electricity output')

#Create variable name as yearh
yearh = ['1991', '1995', '2000', '2005', '2010']
#Create variable for heat map
ind =['CO2 emissions from solid fuel consumption (% of total)','CO2 emissions from liquid fuel consumption (% of total)','Renewable energy consumption (% of total final energy consumption)','Renewable electricity output (% of total electricity output)','CO2 emissions from gaseous fuel consumption (% of total)','Methane emissions (% change from 1990)']
dah = stat_data(data,'Country Name', 'Brazil', yearh , ind)
print(dah.head())
#Calling the function
heat_map(dah)

start = 1961
end = 2016
yeard = [str(i) for i in range(start, end+1)]
ind2 = ['Total fisheries production (metric tons)','CO2 emissions from gaseous fuel consumption (kt)','CO2 emissions from liquid fuel consumption (kt)','Capture fisheries production (metric tons)']
des = stat_data(data,'Country Name', 'Kuwait', yeard , ind2)
#Returns desctiptive statistics summary
summary_stats = des.describe()
print(summary_stats)
skewness = stats.skew(des['Total fisheries production (metric tons)'])
kurtosis = des['CO2 emissions from gaseous fuel consumption (kt)'].kurtosis()
print('Skewness of total fisheries production in Kuwait : ', skewness)
print('kurtosis of CO2 emissions from gaseous fuel consumption in Kuwait : ', kurtosis)
#Save as csv file
summary_stats.to_csv('summary_statistics.csv')



