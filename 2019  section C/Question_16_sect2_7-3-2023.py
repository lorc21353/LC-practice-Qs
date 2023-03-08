# Question 16(b)
# Examination Number:

# For this question it is useful to understand ...
# 1. randint(a, b) returns a random integer N such that a<=N<=b.
# 2. s.append(x) appends the element x to the end of list s.

from random import *

heights = [] # an empty list of heights
weights = [] # an empty list of weights

numOfValues = int(input("Enter the number of pairs of values you wish to generate: "))

# Loop to build up the lists with random values
for count in range(numOfValues):
    # a random integer between 150 and 210
    heights.append(randint(150, 210))
    # a random integer between 50 and 130
    weights.append(randint(50, 130))


bmi_values = []
for i in range(numOfValues):
    bmi_values.append(round((weights[i] / pow(heights[i],2) * 10000), 1))


# Display the lists
print("Heights:", heights)
print("Weights:", weights)
print("BMI values:", bmi_values)