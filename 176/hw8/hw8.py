def calculatetotalbeats(df):
    beats = df["Tempo"] * df["Duration_ms"] / 60000
    result_df = df["Artist", "Track"].copy()

    result_df["Beats"] = beats 
    return result_df 

def checkSingleTrackConsistency(df):
    mask = (df['Album_type'] == "single") & (df['Track'] != df['Album'])

    result = df[mask]["Artist", "Track", "Album,", "Album_type"]
    return result

def isPrime(num):
    if num < 2: 
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if (num % i == 0):
                return False 
            
        return True 
    
def extractPrimeOccurence(df):
    df = df.copy()
    df['Occurence'] = df.groupby('Artist').cumcount() + 1 #total occruence of each track per artist
    
    mask = df['Occurence'].apply(is_Prime)
    result = df[mask]["Artist", "Track", "Occurence"]

    return result 

