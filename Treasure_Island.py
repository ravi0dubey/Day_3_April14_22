print("Welcome to Treasure Island\Your Mission is to find the treasure")
direction = input("Which way you want to go, Left or Right?: ")

if(direction == "Left"):    
    swim_wait =  input("You want to Swim or want to Wait?: ")
    if(swim_wait == "Wait"):
        door = input("Which Door you want to choose (Red, Blue or Yellow) ?: ")
        if (door == "Yellow"):
            print("You Win!")
        else:
            print("Game Over.")    
    else:
        print("Game Over.")  
else:
    print("Game Over.")  
