#create a triangle 

height = int(input("enter triangle height"))
if height < 0:
    print("invalid height")
else:
    for i in range(height):
        spaces = height - i - 1
        stars = i * 2 + 1
        print (" " * spaces + "*" * stars)


"""
Given the daily high temperatures (in Celsius) for 30 days in a list, calculate and display the following:

The average temperature for the month, rounded to one decimal place.
The number of days where the temperature was above the monthly average.
The highest temperature recorded.
The lowest temperature recorded.
The difference between the highest and lowest temperatures.
"""

temperatures = [
    20, 22, 24, 21, 23,
    25, 26, 23, 22, 21,
    24, 26, 27, 28, 29,
    21, 23, 24, 25, 22,
    20, 21, 26, 27, 24,
    22, 20, 21, 23, 24,
]

for temp in temperatures:
    total += temp

monthlyavg = total / 30


for temp in temperatures:  #above monthly average 
    if temp > monthlyavg:
        days += 1


highest = temperatures[0]
lowest = temperatures[0]
for temp in temperatures:
    if temp > highest:
        highest = temp
    elif temp < lowest:
        lowest = temp

temprange = highest - lowest 

