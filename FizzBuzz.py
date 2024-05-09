index = 0
current_number = 0
while True:
    shomarande = [1, 2, 3, 4] 
    shomarande = shomarande[index]
    print(f'hint: current number is: {current_number + 1}')
    index += 1
    current_number += 1
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
                            
        if (current_number % 3 == 0 and p1_choice == -6) or (current_number % 5 == 0 and p1_choice == -10) or (current_number % 15 == 0 and p1_choice == -30):    
            try:
                if p1_choice == -6:
                    p1_choice = "Fizz"
                elif p1_choice == -10:
                    p1_choice = "Buzz"
                elif p1_choice == -30:
                    p1_choice = "FizzBuzz"        
                print(f"P1 said: {p1_choice}")
            except:
                print(f"P1 said: {p1_choice}")
                    
                
        elif p1_choice % 3 != 0 and p1_choice % 5 != 0 and int(p1_choice) % 15 != 0 and p1_choice == current_number:
            print(f"P1 said: {p1_choice}")
        else:
            if p1_choice == -6:
                p1_choice = "Fizz"
            elif p1_choice == -10:    
                p1_choice = "Buzz"
            elif p1_choice == -30:    
                p1_choice = "FizzBuzz"
            print(f"Game is Over!\nP1 said: {p1_choice} but current level must say Fizz, Buzz or FizzBuzz")    
 