import os
"""
The average number of characters per word (int). Round your answer down to the nearest integer.
The length of the longest word in the file (int).
The length of the shortest word in the file (int).
"""

def wordStatistics(filename):

    totalchar = 0
    totalword = 0
    longest = 0
    shortest = float('inf')

    with open (filename, 'r') as file:
        for line in file:
            words = line.split()

            for word in words:
                length = len(word)
                totalchar += length 
                totalword += 1

                if (length > longest):
                    longest = length
                elif (length < shortest):
                    shortest = length 
    average = totalchar / totalword

    return (average, longest, shortest)

def oscarWinners(filename, query):

    winners = []
    with open (filename, 'r') as file:
        header = file.readline()
        for line in file:
            line = line.strip()

        parts = line.split(",", 4) #breaks into 4 seperate parts

        year = parts[1].strip()
        age = parts[2].strip()
        name = parts[3].strip()
        movie = parts[4].strip()

        winners.append(year, age, name, movie)

        namecount = 0 
        total = 0
        if query == 1: 
            for year, age, name, movie in winners:
                if year >= 1960:
                    total += len(name)
                    namecount += 1
            if count == 0:
                return 0
        
            return total / namecount
    
        elif query == 2:
            under40winners = []
            for year, age, name, movie in winners:
                if age < 40:
                    under40winners.append(year, age, name, movie)
            return under40winners
        
        elif query == 3:
            shortest = float('inf')
            shortestrow = []
            for year, age, name, movie in winners:
                if len(movie.replace(" ", "")) < shortest:
                    shortest = len(name)
                    shortestrow = [year, age, name, movie]
            return shortestrow
        
        else:
            return None 

    




def avgCalories(filename):

    dailyvalues = [] #takes in all the values but strips spaces 
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip() #strips spaces 
            if line != "":
                dailyvalues.append(line)

    daysmonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    monthlyaverage = []
    monthsover150k = []

    index = 0
    for month in range(12):
        days = daysmonths[month] #gets the number of days in the month 

        monthdata = dailyvalues[index: index + days]

        total = sum(monthdata)
        average = total // days 

        monthlyaverage.append(average)
        if (total > 150000):
            monthsover150k.append(total)



print(wordStatistics('hw06_p1_example.txt'))
print(avgCalories(hw06_p3_example.txt))
    

