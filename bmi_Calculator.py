# Write a Python Program to create a BMI Calculator.
# Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using 
# a person's weight and height, using this formula: weight / height²

# The resulting number indicates one of the following categories:
# Underweight = less than 18.5
# Normal = more or equal to 18.5 and less than 25
# Overweight = more or equal to 25 and less than 30
# Obesity = 30 or more

# Let’s find out BMI by creating a program that takes a person's weight and height as input and outputs the BMI category.


# asking for input from the users  
height = float(input("Enter height in cm: "))
weight = float(input("Enter weight in kg: "))

# defining a function for BMI  
def BMI(height, weight):
    bmi = weight/(height/100)**2    # formula to calculate BMI
    if (bmi < 16):                  # using if-elif condition
        return 'Severely Underweight', bmi
    elif (bmi >= 16 and bmi < 18.5):
        return 'Underweight', bmi
    elif (bmi >= 18.5 and bmi < 25):
        return 'Healthy', bmi
    elif (bmi >= 25 and bmi < 30):
        return 'Overweight', bmi
    elif (bmi >= 30):
        return 'Obesity', bmi

output, bmi = BMI(height, weight)
print("Your bmi is: {} and  you are: {}". format(bmi,output))