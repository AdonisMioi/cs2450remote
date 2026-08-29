import random

def guess_my_age():
    name = input("Hey! What's your name? ")
    input(f"Hello {name}, im Rotee and i'm going to guess your age!")
        
    low = 15
    high = 40
    attempts = 0

    while True:

        while low <= high:
            guess = random.randint(low, high)
            attempts += 1

            answer = input(f"Are you {guess} years old?(yes,higher,lower): ").strip().lower()

            if answer == 'yes':
                print(f"YOU LIKE THAT! YOU LIKE THAT! {name} is {guess} years old.")
                return

            elif answer == 'higher':
                print("Ewww your old, fine lemme try again!")
                low = guess + 1 
            elif answer == 'lower':
                print("Awww a baby, lemme go again!")
                high = guess - 1  
            else:
                print("cmon stop messin around!")
        
        if low > high:
            print("Cheater cheater pumkin eater! RESTART!!!")
        

guess_my_age()
