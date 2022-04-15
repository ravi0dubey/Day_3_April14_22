
year = int(input("Which year do you want to check? "))
div4= (year%4)
div100= (year%100)
div400= (year%400)

if(div4==0):
    if( div100 ==0 and div400==0):
        print("Leap Year.") 
    elif( div100 != 0 and div400 != 0):
        print("Leap Year.")
    else:
        print("Not Leap year.")
else:
    print("Not Leap Year.")