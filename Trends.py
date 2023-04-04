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
