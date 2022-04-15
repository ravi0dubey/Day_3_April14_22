
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

both_name = name1 + name2
name_lower = both_name.lower()

count_T = name_lower.count("t")
print(f"name: count_T: {count_T}")
count_R = name_lower.count("r")
print(f"name: count_R: {count_R}")
count_U = name_lower.count("u")
print(f"name: count_U: {count_U}")
count_E = name_lower.count("e")
print(f"name: count_E: {count_E}")
count_true_name= count_T + count_R + count_U + count_E
print(f"Count_True:{count_true_name} ")



print(f"count_true: {count_true}")

count_l = name_lower.count("l")
print(f"name: count_l: {count_l}")
count_o = name_lower.count("o")
print(f"name: count_o: {count_o}")
count_v = name_lower.count("v")
print(f"name: count_v: {count_v}")
count_E = name_lower.count("e")
print(f"name: count_E: {count_E}")
count_love_name= count_l + count_o + count_v + count_E
print(f"Count_True:{count_love_name} ")


true_love = str(count_true_name) +str(count_love_name)
print("true_love " + true_love)

num_true_love = int(true_love)

if(num_true_love <10 and num_true_love > 90):
    print(f"Your score is {num_true_love}, you go together like coke and mentos.")
elif(num_true_love >= 40 and num_true_love < 50):
    print(f"Your score is {num_true_love}, you are alright together .")
else:
    print(f"Your score is {num_true_love}")