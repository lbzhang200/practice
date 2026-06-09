import pandas as pd
def mergeWithOption(df1, df2, option=None):
    if option == None:
        return pd.merge(df1, df2, on='Artist_Track', how='inner')
    
    elif option == 0: 
        merged_df = pd.merge(df1, df2, on='Artist_Track', how ='outer')
        return merged_df.fillna(0) #fills missing values with zerores
    
    elif option < 0: 
        merged_df = pd.merge(df1, df2, on='Artist_Track', how='left')
        return merged_df.fillna(abs(option))
    
    elif option > 0:
        merged_df = pd.merge(df1, df2, on = 'Artist_Track', how = 'right')
        return merged_df.fillna(-option)
    
"""
def replicateWithShifts(df): 
    #concat

"""