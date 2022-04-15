print("Welcome to Treasure Island\Your Mission is to find the treasure")
direction = input("Which way you want to go, Left or Right?: ")

if(direction.lower() == "left"):    
    swim_wait =  input("You want to Swim or want to Wait?: ")
    if(swim_wait.lower() == "wait"):
        door = input("Which Door you want to choose (Red, Blue or Yellow) ?: ")
        if (door.lower() == "yellow"):
            print("You Win!")
        else:
            print("Game Over.")    
    else:
        print("Game Over.")  
else:
    print("Game Over.")  
