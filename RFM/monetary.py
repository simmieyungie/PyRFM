# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 19:45:30 2021

@author: SIMIYOUNG
"""

import pandas as pd

def monetary(data, id, spend):
    '''
    This function will calculate the recency.
    data: Dataframe
        
        A dataframe containing at least the customer ID, Transaction/Order Date
    
    id:   String, Integer
        
        (Order/Customer/Transaction) Id column (string or int)
        
    spend: int or float
        
        The cost column either transaction cost
    '''
    #error instance to check if input is either a pandas dataframe and is also not none
    if isinstance(data, pd.DataFrame) == False or data is None:
        raise ValueError("data: Expecting a Dataframe or got 'None'")
    
    #error instance to check if id column is an identified column name
    if id not in data.columns:
        raise ValueError("id: Expected an id (a column) in Dataframe")
    
    #examine the datatype of the date column
    #aggregation to calculate recency
    result = pd.DataFrame(data.groupby(id)[spend].sum()).reset_index()
    
    
    #rename column
    result.rename(columns = {spend : "monetary"}, inplace = True)
    return result


