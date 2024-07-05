import random
x = random.randint(0,100)
g = int(input("How many geusses do you want? "))

for i in range(0,g):
    print("you have", g, "chanses you used:", i  )
    y = int(input("what is your guess?: "))
    if y > x:
        print("The randoe number is lower")
    elif y < x:
        print("the randome number is Higher")
    elif y == x:
        print("you win")
        break
print("the number was", x)