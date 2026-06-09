def testAvg(filename):
    result = {}

    with open (filename, 'r') as file:

        
        for line in file:
            line = line.strip()
            parts = line.split(',') #takes string into array 

            name = parts[0] #name
            score = parts[1:] #scores

            total = 0 
            count = 0 

            for score in scores:
                total += score
                count += 1
            
            avg = total / count 
            result[name] = avg 
    return result 

def salesMonth(filename):
    result = {}

    with open (filename, 'r') as file:
        header = file.readline().strip().split(',') #takes in all months 
        months = header[1:] #all the months 
        rows = []
        for line in file:
            rows.append(line.strip().split(','))

        for monthindex in range(len(months)):
            monthname = months[monthindex]
            maxsales = -1
            best = ""

            for r in rows:
                storename = r[0]
                sales = int(r[monthindex + 1])

                if sales > maxsales:
                    maxsales = sales
                    best = storename 

            result[monthname] = best
    return result 



def lottoWinners(filename):
    with open(filename, 'r') as file:

        winners = []
        for line in file:
            winners.append(line.strip())

        while (True):
            year = int(input("Enter a year in the range 1923 - 2139"))
            if (year == 'quit'):
                break
            elif (year < 1923 or year > 2139): 
                print("yeear not found")
            else:
                index = year - 1923
                winner = winners[index]
                count = winners.count(winner)

                print(f"Year {year}: {winner} {won {count} times}")







            