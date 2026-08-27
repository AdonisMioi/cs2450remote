import random

def guess_my_age():
   name= input("Hey! What's your name?")
   input(f"Hello {name}, im Rotee and i'm going to guess your age!") 
   while True:
       guess = random.randint(15, 40)
       answer = input(f"Are you {guess} years old?(y/n):").strip().lower()

       if answer == 'y': 
           print(f"YOU LIKE THAT! YOU LIKE THAT!{name} is {guess} years old.")
           break
       elif answer =='n':
           print("Awww Rats.")

guess_my_age()
