
#pandas module
import pandas as pd

#define function
def frequency(data, id, bins = {5 : [1,2,3,4,5]}):
    '''
    This function will calculate the recency.
    data: Dataframe
        
        A dataframe containing at least the customer ID, Transaction/Order Date
    
    id:   String, Integer
        
        (Order/Customer/Transaction) Id column (string or int)
        
    bins: dictionary, default 5
        A dictionary containing the number of segments to be created from recency score and the labels associated 
        to quantile groups. The higher the frequency score the more top priority the customer
    '''
    #error instance to check if input is either a pandas dataframe and is also not none
    if isinstance(data, pd.DataFrame) == False or data is None:
        raise ValueError("data: Expecting a Dataframe or got 'None'")
    
    #error instance to check if id column is an identified column name
    if id not in data.columns:
        raise ValueError("id: Expected an id (a column) in Dataframe")
    
    #if bin is not a dictionary, raise error
    if isinstance(bins, dict) == False:
        raise ValueError("bin: Value needs to be an integer. default is 5")
        
    #check if the size of the quartile split is the same as  the labels provided
    if len(list(bins.values())) != int(list(bins.keys())[0]):
        print("Warning: The number of bins for quantile is not same as the label. default is {}".format(bins))
    
    
    #examine the datatype of the date column
    #aggregation to calculate recency
    result = pd.DataFrame(data.groupby(id).size()).reset_index()
    
    #rename size column to frequency
    result.rename(columns = {0 : "frequency"}, inplace = True)
    
    #get bin value from dict
    bin_value = int(list(bins.keys())[0])
    
    #get bin labels from dict
    bin_labels = list(bins.values())[0]
    
    #logic to use bins value
    result["frequency_bins"] = pd.qcut(result.frequency, bin_value, bin_labels)
    #rename column
    
    
    
    return result
