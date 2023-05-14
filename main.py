import random

list1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",1,2,3,4,5,6,7,8,9,"!","@","#","$","%","^","&","*","(",")"]
random.shuffle(list1)

# add a try-except block to handle invalid user input
try:
    user_input = int(input("Enter the length of the password: "))
    password = []
    for i in range(user_input):
        password.append(random.choice(list1))
    random.shuffle(password)
    join = ''.join(map(str, password))
    print(join)

# handle ValueError if user input is not a valid integer
except ValueError:
    print("Invalid input! Please enter a valid integer for the password length.")
