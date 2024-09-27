# Write your program here
# TKTK: Add started code here.
import random
import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

max_guess = int(math.log(larger - smaller + 1, 2))
count = 0
guess = random.randint(smaller, larger)
print("Your number is", guess)
user_hint = input("Enter =, <, or >: ")

while smaller <= larger or larger >= smaller:
    while max_guess > count:
        guess = random.randint(smaller, larger)
        print("Your number is", guess)
        user_hint = input("Enter =, <, or >: ")
        count += 1
        if user_hint == "<":
            larger = guess - 1
            print(smaller, larger)
        elif user_hint == ">":
            smaller = guess + 1
            print(smaller, larger)
        elif user_hint == "=":
            print("Hooray, I've got it in", count, "tries!")
            break
    else:
        print("I'm out of guesses, and you cheated!")
        break
    count += 1
    break
        
