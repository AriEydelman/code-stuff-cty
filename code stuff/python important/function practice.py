# def spicyPrint(inputList):
#     for i in inputList:
       
#         print(i," ",end='')
#     print('\n')


# hat = [1,2,3,4,5]
# spicyPrint(hat)



# def ctyFactorial(num):
#     x = num
#     y = 1

#     for i in range(1, x+1):
#          y = y * i
#     print( "here is your answer: "  )
#     print(y)

# ctyFactorial(7)


# def convertSebtanceUpper(sentence):
#     print(len(sentence))

# convertSebtanceUpper("hot")



def discout_calc(x):
    t=[]
    for i in x:
        discontTemp=i*.2 # Calculates Discount
        t.append(discontTemp)
    
    return t

a=discout_calc([10,20,30,40,50])
print(a)



