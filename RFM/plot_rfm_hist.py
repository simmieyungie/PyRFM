
#RFM histogram
import matplotlib.pyplot as plt


def plot_rfm_hist(rfm_table):
    '''
    This function will return a histogram distribution of rfm values.
    rfm_table: Dataframe
        
        A dataframe containing at least recency, frequency and monetary columns. It's to be used
        particularly after using the rfm function
    '''
      #error instance to check if input is either a pandas dataframe and is also not none
    if isinstance(rfm_table, pd.DataFrame) == False or rfm_table is None:
        raise ValueError("data: Expecting a Dataframe or got 'None'")
        
    if "recency" not in rfm_table.columns:
        raise ValueError("recency: recency column not found in column names, add 'recency'")
        
    if "frequency" not in rfm_table.columns:
        raise ValueError("frequency: recency column not found in column names, add 'frequency'")
        
    if "monetary" not in rfm_table.columns:
        raise ValueError("monetary: recency column not found in column names, add 'monetary'")
        
    fig, ax = plt.subplots(1,3, figsize = (10, 5)) #one row, three columns
    #recency
    ax[0].hist(rfm_table.recency)
    ax[0].set_title("Recency")
    #frequency
    ax[1].hist(rfm_table.frequency)
    ax[1].set_title("Frequency")
    #monetary
    ax[2].hist(rfm_table.monetary)
    ax[2].set_title("Monetary")
    plt.show()
    
    return 
