# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 19:45:21 2021

@author: SIMIYOUNG
"""

import pandas as pd

def recency(data, id, date):
    '''
    This function will calculate the recency.
    data: Dataframe
        
        A dataframe containing at least the customer ID, Transaction/Order Date
    
    id:   String, Integer
        
        (Order/Customer/Transaction) Id column (string or int)
    
    date: Date, Datetime, Object

        A date column (NB: A type conversion will be attempted by the function but you can also ensure the date type is proper)
    threshold: An integer value, specifying how many days should be considered
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
       
    #aggregation to calculate recency
    result = data.groupby(id) \
            .agg({date: lambda date: (date.max() - date.min()).days})\
            .reset_index() #reset index
    
    #rename column
    result.rename(columns = {date : "recency"}, inplace = True)
    return result


