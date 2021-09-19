import pandas as pd

#define the function
def recency(data, id, date, present_date, bins = {5 : [5,4,3,2,1]}):
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
    if data.dtypes[date].name not in ["datetime64[ns]", "datetime.datetime"]:
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
    
    #rename column
    result.rename(columns = {date : "recency"}, inplace = True)
    
    #get bin value
    bin_value = int(list(bins.keys())[0])
    
    #get bin labels
    bin_labels = list(bins.values())[0]
    
    #logic to use bins value
    result["recency_bins"] = pd.qcut(result.recency, bin_value, bin_labels)
    
    #note that if bin changes then label needs to change also
    
    
    return result
