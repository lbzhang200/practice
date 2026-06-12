#generates max profit throughout an array 
def maxprofit(prices):
    minprice = float('inf')
    maxprofit = 0

    for price in prices:
        if price < minprice: 
            minprice = price 
        elif price - minprice > maxprofit:
            maxprofit = price - minprice 

    return maxprofit 

prices = [7, 1, 5, 3, 6, 4]
print(maxprofit(prices))  # 5

def maxprofit(prices):
    minprice = float('inf')
    maxprofit = 0

    for price in prices:
        if price < minprice:
            minprice = price 
        elif price - minprice > maxprofit: 
            maxprofit = price - minprice 

    return maxprofit 