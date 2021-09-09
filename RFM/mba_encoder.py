def mba_encoder(data, id_col, product_col):
    '''
    This function will preprocess and return a one-hot encode matrix of ID's and products.
    data: Dataframe
        
        A dataframe containing at least the customer ID, Transaction/Order Date
    
    id_col:   String
        
        column name containing ID
    
    product_col: String
        
        Column name containing product col
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
    
    
    
    
