#official start to pandas 
import pandas as pd
def removeDuplicates(df):

    new_df = df['Artist', 'Track', 'Album', 'Duration_ms'].copy()

    new_df = new_df.drop_duplicates()
    new_df = new_df.sort_values(by="Duration_ms", asecnding = True)
    return new_df 

def handleMissing(df, n):
    new_df = df['Energy', 'Title', 'Channel', 'Views', 'Stream'].copy()
    if n >= 0: 
        new_df = new_df.fillna(n) #fills all missing values with n

    else:
        new_df = new_df.dropna() #drops all rows with missing value 

    return new_df 

def processArtists(df):
    new_df = df["Artist", "Track", "Key", "Stream"].copy()
    new_df = new_df[new_df["Artist"].str.isalpha() == True]
    new_df = new_df.drop_duplicates()
    new_df = new_df.set_index("Artist")
    new_df["Stream"] = new_df["Stream"].interpolate(method = 'linear')

    return new_df 