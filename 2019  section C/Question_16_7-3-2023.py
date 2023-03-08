# Question 16(a)
# Examination Number:

def display_intro():
 print("Welcome to my BMI calculator!")

display_intro()

weight = int(input("Enter weight (in kilograms): ")) # read weight
height = int(input("Enter height (in centimeters): ")) # centimetres

bmi = weight / pow(height,2) * 10000

category = ""
if bmi < 18.5:
    category = "Underweight"
elif bmi <= 24.9:
    category = "Normal"
elif bmi <= 29.9:
    category = "Overweight"
elif bmi >= 30:
    category="Obese"

print("BMI is: ", round(bmi,1))
print(category)