# from random import randint

# number = randint(1, 999)
# print(f"the random number is {number}")
# if number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# elif number % 15 == 0 and number % 5 == 0:
#     print("FizzBuzz")        
# else:
#     print(number)    
    
# while True:
#     number = 1
    
#     print("Player1...\n")
#     player1 = int(input("Enter the number: "))
    
#     if player1 % 3 != 0 and player1 % 5 != 0 and player1 % 15 != 0:
#         if player1 == number:
#             print("player2\n")
#         elif player1 != number:
#             print(f"Game is Over!\nplayer1 enterd {player1} and that was {number}")
#             break
            
#     elif player1 % 3 == 0 or player1 % 5 == 0 or player1 % 15 == 0:
#         if number % 3 == 0:
#             print("Fizz")
#             print("player2...\n")
#             continue
#         elif number % 5 == 0:
#             print("Buzz")
#             print("player2...\n")
#             continue
#         elif number % 15 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#             print("player2...\n")   
#             continue
        
#     number += 1           
#     player2 = int(input("Enter the number: "))     
#     if player2 % 3 != 0 and player2 % 5 != 0 and player2 % 15 != 0:
#         if player2 == number:
#             print("player3...\n")
#         elif player2 != number:
#             print(f"Game is Over!\nplayer2 enterd {player2} and that was {number}.")
#             break
            
#     elif player2 % 3 == 0 or player2 % 5 == 0 or player2 % 15 == 0:
#         if number % 3 == 0:
#             print("Fizz")
#             print("player3...\n")
#             continue
#         elif number % 5 == 0:
#             print("Buzz")
#             print("player3...\n")
#             continue
#         elif number % 15 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#             print("player3...\n")   
#             continue      

index = 0
current_number = 0
while True:
    shomarande = [1, 2, 3, 4] 
    shomarande = shomarande[index]
    print('shomarande: ', shomarande)
    index += 1
    current_number += 1
    print('current_number: ', current_number)
    if index == 4:
        index = 0 
        
    if index == 1:    
        p1_choice = input("P1) Enter your number: ").lower()
        try:
            p1_choice = int(p1_choice)
        except:
            if p1_choice == "fizz":
                p1_choice = -6
            elif p1_choice == "buzz":
                p1_choice = -10
            elif p1_choice == "fizzbuzz":
                p1_choice == -30
                            
        # if (current_number % 3 == 0 and p1_choice == "Fizz") or (current_number % 5 == 0 and p1_choice == "Buzz") or (current_number % 15 == 0 and p1_choice == "FizzBuzz"):    
        if (current_number % 3 == 0 and p1_choice == -6) or (current_number % 5 == 0 and p1_choice == -10) or (current_number % 15 == 0 and p1_choice == -30):    
            try:
                if p1_choice == -6:
                    p1_choice = "Fizz"
                elif p1_choice == -10:
                    p1_choice = "Buzz"
                elif p1_choice == -30:
                    p1_choice = "FizzBuzz"        
                print(f"P1 saied: {p1_choice}")
            except:
                print(f"P1 saied: {p1_choice}")
                    
                
        elif p1_choice % 3 != 0 and p1_choice % 5 != 0 and int(p1_choice) % 15 != 0 and p1_choice == current_number:
            print(f"P1 saied: {p1_choice}")
        else:
            if p1_choice == -6:
                p1_choice = "Fizz"
            elif p1_choice == -10:    
                p1_choice = "Buzz"
            elif p1_choice == -30:    
                p1_choice = "FizzBuzz"
            print(f"Game is Over!\nP1 saied: {p1_choice} but current level must say Fizz, Buzz or FizzBuzz")    
            
    # elif index == 2:              
    #     p2_choice = int(input("P2) Enter your number: "))
    #     print(f"P2 saied: {p2_choice}")
    # elif index == 3:              
    #     p3_choice = int(input("P3) Enter your number: "))
    #     print(f"P3 saied: {p3_choice}")
    # else:              
    #     p4_choice = int(input("P4) Enter your number: "))
    #     print(f"P4 saied: {p4_choice}")          
    
    # elif type(p1_choice) == str:
            # print(f"Game is Over!\nP1 saied: {p1_choice} but current level must say Fizz, Buzz or FizzBuzz")
        