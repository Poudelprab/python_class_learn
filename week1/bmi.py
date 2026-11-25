weight= float(input("Enter your weight in kg: "))
height= float(input("Enter your height in meters: "))
BMI  = weight/(height**2) #formula to calculatte BMI
print(f"Your BMI is: {BMI:.3f}") #displaying calculated BMI with 3 decimal places