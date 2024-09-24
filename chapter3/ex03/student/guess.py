# Write your program here
# TKTK: Add started code here.
import random
from math import log

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0

while True:
    count += 1
    userNumber = int(input("Enter your number: "))
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print("Congratulations! The computer guessed in", count, "tries!")
        break