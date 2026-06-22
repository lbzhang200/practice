import pandas as pd
import numpy as np

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
    
def replicateWithShifts(df): 
    segments = []

    for i in range(len(df.columns)):
        segment = df.copy()

        colstonan = df.columns[:i]
        segment[colstonan] = np.nan
        segments.append(segment)

    result = pd.concat(segments, ignore_index=True)
    return result 


    
def binByDigitLength(df):
    df_binned = df.copy() #creates a new copy
    
    numeric_cols = df_binned.select_dtypes(include=[np.number]).columns #filters only the columns with numbers 
    
    for col in numeric_cols: #iterates through the numerical columns
        def get_bin(val): #helper function to categorize an inidividual value
            if pd.isna(val): #check if value is null
                return "[0, 1)" # NaN treated as 0 digits
            int_part = int(abs(val)) #takes in integer of abs value
            
            if int_part == 0:
                return "[0, 1)"
            
            num_digits = len(str(int_part)) #takes in string part of int_part
            lower = 10**(num_digits - 1) #lower bound 
            upper = 10**num_digits #upper bound
            
            return f"[{lower}, {upper})" #returns lower and upper bound
        
        df_binned[col] = df_binned[col].apply(get_bin) #apply new transformation to column 
        
    return df_binned



