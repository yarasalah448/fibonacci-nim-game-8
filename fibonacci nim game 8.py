######### FIBONACCII NIMM GAMEE #########

### PLAYER 1 ###

def player1 ():

    global turns
    global number_of_coins
    global coins_of_player1
    global coins_of_player2
    global intplayer1
    coins_of_player1=(input("player 1 Enter a number of coins :\n"))

    ## all fail cases
    while not coins_of_player1.isdigit():
       coins_of_player1 = (input(" player 1 Enter a number, please! :\n"))
    intplayer1 = int(coins_of_player1)
    if turns == 0:
        while intplayer1>=number_of_coins:
            intplayer1=int(input(" player 1 Enter a number that are less than the total number of coins : \n"))
        number_of_coins=number_of_coins-intplayer1
        print ("Now,the available number of the total coins is : " ,number_of_coins)
        turns+=1
    else:
        while intplayer1 > intplayer2*2:
            coins_of_player1=int(input(" player 1Enter a number at most twice of your opponent's coins :\n"))
        number_of_coins=number_of_coins-intplayer1
        print ("Now,the available number of the total coins is : " ,number_of_coins)


### PLAYER 2 ###

def player2():
   
    global number_of_coins
    global coins_of_player1
    global coins_of_player2
    global intplayer2

    coins_of_player2=(input(" player 2 Enter a number of coins : \n"))

    ## all fail cases 
    while not coins_of_player2.isdigit():
        coins_of_player2 = (input(" Enter a number, please!  :\n"))
    intplayer2 = int(coins_of_player2)
    
    while intplayer2 > number_of_coins:
        intplayer2=int(input(" player 2 Enter a number that are less than the total number of coins : \n "))
    while intplayer2 > intplayer1*2:
        coins_of_player2=int(input("  player 2 Enter number at most twice of your opponent's coins :\n"))
    number_of_coins=number_of_coins-intplayer2
    print(" Now,the number of  the available coins is : " , number_of_coins)
    
  

### MAIN CODE OF FIBONACCI NIM GAME ###
    
def fibonacci_nim ():
    global name_of_player1
    global name_of_player2
    global number_of_coins
    name_of_player1=str(input("player 1  enter your name or anything  that expresses you : \n"))
    name_of_player2=str(input("player 2  enter your name or anything  that expresses you : \n"))
    if name_of_player1 == name_of_player2:
        name_of_player2=str(input(" Enter your second name also or your nickname to distinguish between you and your opponent : \n"))
    number_of_coins=int(input("Enter a number of coins : \n"))
    print(" The number of  the total coins is " , number_of_coins)
    
    while True:
        player1()
        if number_of_coins==0:
            print(name_of_player1 , " is the winner!")
            break
        
        player2()
        if number_of_coins==0:
            print(name_of_player2 , " is the winner!")
            break
  

number_of_coins=0
turns=0


fibonacci_nim()