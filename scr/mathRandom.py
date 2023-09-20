# this module is a guessing game as an example of math random

# import the math package with as you can rename a package like in SQL
import random as r

lower_bound = 1
upper_bound = 100
# picks a number between 1 and 100
computer_pick = r.randint(lower_bound, upper_bound)

print("Ich denke an eine Zahl zwischen", lower_bound, " und ", upper_bound)

user_guess = int(input("Rate: "))
guess_count = 1

while user_guess != computer_pick:
    print("Falsch! ")
    if user_guess > computer_pick:
        print("Die gesuchte Zahl ist kleiner. ")

    else:
        print("Die gesuchte Zahl ist grösser. ")
    user_guess = int(input("Rate: "))
guess_count += 1

print("Richtig geraten! :-) ")
print("Anzahl verusche: ", guess_count)

