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



        


print(wordStatistics('hw06_p1_example.txt'))
    

