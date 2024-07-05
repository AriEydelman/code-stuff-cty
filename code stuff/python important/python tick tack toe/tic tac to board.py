def cool_gamebourad(n):
    for i in range(0, len(n)):
        print(n[i])

gameboard= [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
    ]
endthegame = False

while(endthegame == False):
    x = int(input("what row do you wana go in?"))
    y = int(input("what column do you ana go in ?"))
    z = int(input("what player are you ?"))
    if gameboard[x][y] == "_":
        gameboard[x][y] = z
        cool_gamebourad(gameboard)
    else:
        print("nah man you realy tried to cheat get out just leave you lose")
        endthegame = True    
    if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] != "_":
        print("u win")
        endthegame = True
    if gameboard[0][2] == gameboard[1][1] == gameboard[2][0] != "_":
        print("u win")
        endthegame = True
    for i in range(0,3):
        if gameboard[0][i] == gameboard[1][i] == gameboard[2][i] != "_":
            print("u win")
            endthegame = True
    for i in range(0,3):
        if gameboard[i][0] == gameboard[i][1] == gameboard[i][2] != "_":
            print("u win")
            endthegame = True
        






