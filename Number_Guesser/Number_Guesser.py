import random

while True:
    num = input("Type in a number to start the game: ")
    # takes away - in case there is one and checks if it's a digit or not
    if not num.lstrip("-").isdigit():
        print("Type in a number not a letter to start the game")
        # if not it continues with the next while iteration and start from beginning
        continue
    num = int(num)
    if num <= 0:
        print("Type in a number bigger than 0 to start the game")
    if num > 0:
        # if the number is bigger than 0 it goes out of the while loop
        break

rand_num = random.randint(0, num)
print("You typed in ", num)
print("That means you will get a random number between 0 and ", num)
# now we start with the user guessing
while True:
    num2 = input("What do you think which random number you have? Type in a positive number: ")
    num2 = int(num2)
    if num2 == rand_num:
        print("wow, you got it right! Congrats :-) ")
        break
    elif num2 <= rand_num:
        print("Your number should be bigger")
    elif num2 >= rand_num:
        print("Your number should be smaller")










