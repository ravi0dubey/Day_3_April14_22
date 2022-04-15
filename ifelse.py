
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
sex = input("Enter Your Sex(M of F): ")
bmi = round(weight/(height**2))
heightsq = height**2
print(heightsq)
print(bmi)
if (sex== "M"):
  if(bmi<18):
    print(f"Your BMI is {bmi}, you are underweight.")
  elif(bmi>=19 and bmi<25):
    print(f"Your BMI is {bmi}, you have a normal weight.")
  elif(bmi>=25 and bmi<30):
    print(f"Your BMI is {bmi}, you are slightly overweight.")
  elif(bmi>=30 and bmi<35):
    print(f"Your BMI is {bmi}, you are obese.")
 else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
else:
  if(bmi<16):
    print(f"Your BMI is {bmi}, you are underweight.")
  elif(bmi>=16 and bmi<23):
    print(f"Your BMI is {bmi}, you have a normal weight.")
  elif(bmi>=23 and bmi<28):
    print(f"Your BMI is {bmi}, you are slightly overweight.")
  elif(bmi>=28 and bmi<33):
    print(f"Your BMI is {bmi}, you are obese.")
  else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
