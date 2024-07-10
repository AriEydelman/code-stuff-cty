import random

quit_game = False

money = 100

points = 0

game = True

quit_game = False

hit = True

house_points = 0

    

while money == 0 or quit_game == False:
    
    

    deack = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    print("to end the game you have to have 0 credits or enter q in the input when it asks ")

    while game == True:

        

        end = input(" if you want to stop playing click q: ")
        if end == "q":
            quit_game == True

        moneybet = int(input("how much do you wana bet you have {}: ".format(money)))

        hit = True
        house_hit = True
        points = 0
        while house_hit == True:
            
            card1 = random.randint(0,12)

            if house_points <= 17:
                house_points += deack[card1]
            else:
                house_hit = False
            print("house has {} points".format(house_points))


        while hit == True:

            card = random.randint(0,12)

            if card == 0:
                ace = int(input("what do you want your ace to be type 1 or 11: "))
                if ace == 1:
                    points += 1
                elif ace == 11:
                    points += 11
                print("unless you got ace then you got {}".format(ace))


            else:
                print("you got{}".format(deack[card]) )

                points+=deack[card]

                print("you have {} points".format(points))

                
                    
                if points > 21:
                    print("sry that a bust house always wins")
                    money -= moneybet
                    hit = False

                elif points == 21:
                    money += moneybet
                    hit = False
                
                run = int(input("do you wana hit or not say 1 for yes or 0 for no: "))            
                if run == 0:
                    hit=False
                if hit == 1:
                    hit=True

                elif hit == False:
                    if points < house_points:
                        print("let me get that cash")
                        money -= moneybet
                        hit = False

                    elif points > house_points:
                        money += moneybet
                        hit = False
                        # points dont work cus house points