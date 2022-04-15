print("Welcome to Roller Coaster Ride")
height = int(input("Please enter your height in cm: "))
if (height >= 180):
  age = int(input("Enter your age: "))
  if age < 12:
    print("You are eligible for child ticket of $5.")
    ticket_price = 5
  elif(age>=12 and age<18):
    print("You are eligible for Youth ticket of $7.")
    ticket_price = 7
  elif(age>=45 and age<=50):
    print("You are Midlife crisis person ticket is free.")
    ticket_price = 0
  else:
    print("You are eligible for Adult ticket of $12.")
    ticket_price = 12
  photo_need = input("Do you want to get your photo clicked(Y/N)?.")
  if(age>=45 and age<=50 and photo_need == "Y"):
    print("You just have to pay $3 for photo.")
    ticket_price += 3
  elif(photo_need == "Y"):
    print("plus $3 for photo.")
    ticket_price += 3
    
  print(f"Please pay total $ {ticket_price}")
else:
  print("Sorry, you have to grow taller")
    
#number = int(input("Enter the value: "))
#mod_value = number % 2
#if(mod_value == 0):
#  print("Its an even number")
#else:
#  print("Its an Odd number")

  
    