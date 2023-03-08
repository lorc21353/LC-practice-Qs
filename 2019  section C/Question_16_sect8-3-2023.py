# Question 16(c)
# Examination Number:

# set w to n on an ordered list, count down until w is equal to -1
# if the new number is the same as the last do not reduce w
# when w is equal to zero that is the nth largest value of the list
def find_nth_largest(n, list_of_values): 
    w = n
    vals = list_of_values
    previous = 0
    for i in reversed(vals):
        if i != previous:
            w-=1
            print(w)
        if w == 0:
            return i
        previous = i
            

bmi_values = [24, 19, 33, 35, 27, 18, 15, 33, 35, 23, 32, 23]
bmi_values.sort()
print(bmi_values)
count = 0 
# go through the list and count all nums higher than 30
for i in bmi_values:
    if i >= 30:
        count+=1
        
print("Obese:", count)

biggest = 0
second_biggest = 0 
for i in reversed(bmi_values):
    if i >= biggest:
        biggest = i
    elif i > second_biggest:
        second_biggest = i
        
print("Largest:", biggest)
print("Second Largest:", second_biggest)
print(find_nth_largest(3, bmi_values)) 
