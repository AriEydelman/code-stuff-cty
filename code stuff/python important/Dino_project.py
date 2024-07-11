def cool_gamebourad(n):
    for i in range(0, len(n)):
        print(n[i])

    

Dino = "🧍"

z = 1
y = 1

gameboard= [
    [" # "," # "," # "," # "," # "],
    [" # "," 🧍"," _ "," _ "," # "],
    [" # "," # "," # "," _ "," # "],
    [" # "," # "," # "," _ "," # "],
    [" # "," _ "," _ "," _ "," # "],
    [" # "," _ "," # "," # "," # "],
    [" # "," _ "," _ "," _ "," E "],
    [" # "," # "," # "," # "," # "]
]

win = False
while win == False:
    cool_gamebourad(gameboard)


    x = input("wasd: ")

    gameboard[z][y] = " _ "

    if x == "w":
        z -= 1
    
    if x == "a":
        y -= 1
   
    if x == "s":
        z += 1
   
    if x == "d":
        y += 1


    if gameboard [z][y] == " # ":
        if x == "w":
            z += 1
    
        if x == "a":
            y += 1
   
        if x == "s":
            z -= 1
   
        if x == "d":
            y -= 1
        
        gameboard[z][y] = "🧍"

        continue
    
    
    
    gameboard[z][y] = "🧍"


    if Dino == gameboard[6][4]:
        win = True  
    else: 
        continue

    