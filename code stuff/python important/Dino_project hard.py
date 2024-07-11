def cool_gameboard(n):
    for i in range(0, len(n)):
        print(" ")
        for j in range(0, len(n[i])):
            print(f"{n[i][j]}", end=" ")
    print("\n")
            
    

Dino = "🧍"

z = 1
y = 1

c = 1
r = 2

gameboard= [
    [" # "," # "," _ "," _ "," # "," # "],
    [" # "," 🧍"," ☐ "," _ "," _ "," # "],
    [" # "," # "," # "," _ "," _ "," # "],
    [" # "," # "," _ "," _ "," _ "," # "],
    [" # "," _ "," _ "," _ "," 🪤 "," # "],
    [" # "," _ "," # "," # "," # "," # "],
    [" # "," _ "," _ "," _ "," E "," # "],
     [" # "," # "," # "," # "," # "," # "]
]

win = False
while win == False:
    cool_gameboard(gameboard)

    if z < 0 or y < 0 or c < 0 or r < 0:
        win = True

    x = input("wasd: ")

    gameboard[z][y] = " _ "

    if x == "w":
        z -= 1

    
    elif x == "a":
        y -= 1
   
    elif x == "s":
        z += 1
   
    elif x == "d":
        y += 1


    if gameboard [z][y] == " # ":
        if x == "w":
            z += 1
    
        elif x == "a":
            y += 1
   
        elif x == "s":
            z -= 1
   
        elif x == "d":
            y -= 1
        
        gameboard[z][y] = "🧍"

        


    if gameboard [z][y] == gameboard [c][r]:

        if x == "w":
            c -= 1
            if gameboard [c][r] == " # ":
                c += 1
                z += 1


        elif x == "a":
            r -= 1
            if gameboard [c][r] == " # ":
                r += 1
                y += 1


        elif x == "s":
            c += 1
            if gameboard [c][r] == " # ":
                c -= 1
                z -= 1


        elif x == "d":
            r += 1
            if gameboard [c][r] == " # ":
                r -= 1
                y -=1


        gameboard[c][r] = " ☐ "



    gameboard[z][y] = "🧍"
    gameboard[c][r] = " ☐ "

    if Dino == gameboard[6][4] and gameboard[c][r] == gameboard[4][4] :
        win = True  
    else: 
        gameboard[6][4] = " E "
        gameboard[4][4] = " 🪤 "
        continue