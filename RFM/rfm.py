# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:15:09 2021

@author: SIMIYOUNG
"""

#import sys
#sys.path.append(r'C:/Users/SIMIYOUNG/Documents/Python-Projects/RFM/PyRFM/RFM')

#import RFM.recency

import pandas as pd

import recency, frequency, monetary

def rfm(data, id, date, present_date, spend, bins = {5 : [5,4,3,2,1]}):
    '''
    This function will calculate the recency.
    data: Dataframe
        
        A dataframe containing at least the customer ID, Transaction/Order Date
    
    id:   String, Integer
        
        (Order/Customer/Transaction) Id column (string or int)
    
    date: Date, Datetime, Object

        A date column (NB: A type conversion will be attempted by the function but you can also ensure the date type is proper)
    threshold: An integer value, specifying how many days should be considered
    
    present_date: datetime 
        The present date or most recent date to serve as a reference point for recency
        
    bins: dictionary, default 5
        A dictionary containing the number of segments to be created from recency score and the labels associated 
        to quantile groups. NB: that for Recency Score we need to give inverse labels as the more active 
        the customer is the lower the value of Recency i
    '''
    #error instance to check if input is either a pandas dataframe and is also not none
    if isinstance(data, pd.DataFrame) == False or data is None:
        raise ValueError("data: Expecting a Dataframe or got 'None'")
    
    #error instance to check if id column is an identified column name
    if id not in data.columns:
        raise ValueError("id: Expected an id (a column) in Dataframe")
    
    #examine the datatype of the date column
    if data.dtypes[date].name != "datetime64[ns]":
        raise ValueError("date: Expected a date datatype, 'convert the date/datetime type'")
        #print("This Column is not a of date/datetime data type")
    
    if present_date is None:
        raise ValueError("present_date: Specify the recent date to calculate recency")
    #aggregation to calculate recency
    result = data.groupby(id) \
            .agg({date: lambda date: (present_date - date.max()).days})\
            .reset_index() #reset index
    
    if isinstance(bins, dict) == False:
        raise ValueError("bin: Value needs to be an integer. default is 5")
    
    if len(list(bins.values())) != int(list(bins.keys())[0]):
        print("Warning: The number of bins for quantile is not same as the label. default is {}".format(bins))
    
    
    #recency
    a = recency(data = data, id = id, date = date, present_date = present_date, bins = bins)
    
    #frequency 
    #drop id column
    b = frequency(data = data, id = id, bins = bins).drop(id, axis = 1)
    
    #monetary
    #drop id column
    c = monetary(data = data, id = id, spend = spend, bins = bins).drop(id, axis = 1)
    
    #append results
    result = pd.concat([a, b, c], axis = 1)
    
    #add rfm column
    #concatenate rfm columns individual bin values to get the final rating of each customer
    result["RFM"] = result.recency_bins.astype(str) + result.frequency_bins.astype(str) + result.monetary_bins.astype(str)
    
    return result
    