

gamebord= [
    [1,0,0],
    [2,0,0],
    [3,0,0]
]

endthegame = False


while(endthegame == False):
    for i in gamebord:
        x = input("what row do you wana go in?")
        y = input("what colume do you ana go in")
        z = input("what player are u")
        gamebord[x][y] = z
        print(gamebord)

        






