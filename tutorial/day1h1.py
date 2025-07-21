#Build a BMI calculator (Input: height, weight → Output: BMI & category).

height=float(input("Enter your height :"))
weight=float(input("Enter your weight :"))
BMI=(weight/(height*height))
print(BMI)
if BMI<18.5:
    print("Underweight")
elif 18.5<BMI<25:
    print("Healthy")
elif 25<BMI<30:
    print("over Wieght")
else:
    print("obesity")            