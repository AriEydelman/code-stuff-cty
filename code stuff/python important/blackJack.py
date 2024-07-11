import random

quit_game = False

money = 100

points = 0

game = True

quit_game = False

hit = True

house_points = 0

house_hit = True

    

while money > 0 and quit_game == False:
    
    

    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    print("to end the game you have to have 0 credits or enter q in the input when it asks ")

    while game == True:

        if money == 0:
            money = 0
            game = False
            quit_game = True
            hit = False
            house_hit = False
        end = input(" if you want to stop playing click q: ")
        if end == "q":
            money = 0
            game = False
            quit_game = True
            hit = False
            house_hit = False
        else:
            moneybet = int(input("how much do you wana bet you have {}: ".format(money)))
            if moneybet > money or moneybet <= 0:
                print("cant do that")
                exit()
            hit = True
            house_hit = True
            points = 0
            house_points = 0
        while house_hit == True:
                
            card1 = random.randint(0,12)

            if house_points <= 17:
                house_points += deck[card1]
            else:
                house_hit = False
            print("house has {} points".format(house_points))

            if house_points > 21:
                money += moneybet
                house_hit = False
                hit = False


        while hit == True:

            if money <= 0 and quit_game == False:
                print("you know your out of mony why did you try to play fine i will let you have this last round")
            card = random.randint(0,12)

            if card == 0:
                ace = int(input("what do you want your ace to be type 1 or 11: "))
                if ace == 1 or ace == 11:
                    ace = ace
                else:
                    print("cant do that")
                    exit()
                if ace == 1:
                    points += 1
                elif ace == 11:
                    points += 11
                print("you picked {}".format(ace))
                print("you have {} points".format(points))


                
            else:
                print("you got{}".format(deck[card]) )

                points+=deck[card]

                print("you have {} points".format(points))

                
                    
                if points > 21:
                    print("sry that a bust house always wins")
                    money -= moneybet
                    hit = False

                elif points == 21:
                    money += moneybet
                    hit = False


                        # points dont work cus house points

            run = int(input("do you wana hit or not say 1 for yes or 0 for no: "))   
            if run == 1 or run ==0:
                run =run
            else:
                print("cant do that")
                exit()         
            if run == 0:
                hit=False

            if hit == 1:
                hit=True

            elif hit == False:
                
                if points < house_points:
                    print("let me get that cash")
                    money -= moneybet
                    hit = False

                elif points > house_points and points <= 21:
                    money += moneybet
                    hit = False