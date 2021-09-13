def mba_encoder(data, id_col, product_col, quantity_col, summary_criteria = None):
    '''
    This function will preprocess and return a one-hot encode matrix of ID's and products.
    data: Dataframe
        
        A dataframe containing at least the customer ID, Transaction/Order Date
    
    id_col:   String
        
        Column name containing ID
    
    product_col: String
        
        Column name containing product col
        
    quantity_col: String
    
        Column name containing quantity of product purchase
        
    summary_criteria: Dict
        
        A dictionary containing summary criteria
    '''
    #error handlers
    #error instance to check if input is either a pandas dataframe and is also not none
    if isinstance(data, pd.DataFrame) == False or data is None:
        raise ValueError("data: Expecting a Dataframe or got 'None'")
    
    #error instance to check if id column is an identified column name
    if id_col not in data.columns:
        raise ValueError("id: Expected a valid id column name in Dataframe 'data'")
    
     #error instance to check if product column is an identified column name
    if product_col not in data.columns:
        raise ValueError("id: Expected a valid product column name in Dataframe 'data'")
    
    #error handler if instance for summary_criteria if 
    if summary_criteria != None and isinstance(summary_criteria, dict) == False:
        raise TypeError("summary_criteria: Expected a dict dtype if summary_criteria is not 'None'")
    
    #if data is to be summarised
    if summary_criteria != None and isinstance(summary_criteria, dict) == True:
        summary = list(summary_criteria.keys()) 
        cols = list(summary_criteria.values())
        
        data.groupby([summary])
        
    
    
    
    #Encoding
    basket = data \
    .unstack() \
    .reset_index()
    .set_index(id_col)
    
    
    
    return basket
