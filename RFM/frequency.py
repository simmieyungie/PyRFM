# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 19:45:21 2021

@author: SIMIYOUNG
"""
import pandas as pd

def frequency(data, id):
    '''
    This function will calculate the recency.
    data: Dataframe
        
        A dataframe containing at least the customer ID, Transaction/Order Date
    
    id:   String, Integer
        
        (Order/Customer/Transaction) Id column (string or int)
    '''
    #error instance to check if input is either a pandas dataframe and is also not none
    if isinstance(data, pd.DataFrame) == False or data is None:
        raise ValueError("data: Expecting a Dataframe or got 'None'")
    
    #error instance to check if id column is an identified column name
    if id not in data.columns:
        raise ValueError("id: Expected an id (a column) in Dataframe")
    
    #examine the datatype of the date column
    #aggregation to calculate recency
    result = pd.DataFrame(data.groupby(id).size()).reset_index()
    
    
    #rename column
    result.rename(columns = {0 : "frequency"}, inplace = True)
    return result