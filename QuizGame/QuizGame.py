print("Hello, welcome to my self-created Quiz game, let's see how much you know. ;-) ")
StartGame = input("If you're ready to play type in yes: ")

if StartGame.lower() != "yes":
    print("Okay that means no playing time today, then let's play another time :-( hope you come back soon ")
    quit()

print("That's great!! Let's start: ")

# initializing Answer count
count = 0
print("......... ")
# 1 #################################################################
Answer1 = input("1. What's the capital of Italy? ")
if Answer1.lower() == "rome":
        print("First Answer is right, Congratulations! Let's go on..")
        count += 1
else:
    print("Oh noo, you missed that one - keep trying!")
print("......... ")
# 2 #################################################################
Answer2 = input("2. What's the name of the current leader of Russia? ")
if Answer2.lower() == "putin":
    print("You know something about politics - I'm surprised :-P !")
    count += 1
    if count == 2:
        print("that's a double streak - keep grinding! ")
else :
    print("Oh noo, you missed that one - you can do better!")
print("......... ")
# 3 #################################################################
Answer3 = input("3. Which car brand has a horse on their logo? ")
if Answer3.lower() == "ferrari" or Answer3.lower() == "porsche":
    print("You got it, seems like you have an eye for luxury cars! ;-) ")
    count += 1
    if count == 3:
        print("PS: That was a Three times streak - Awesome! ")
else :
    print("You got something wrong here, seems like someone is not that into cars :-( ")
print("......... ")
# 4 #################################################################
Answer4 = input("4. What's the name of the place where the city hall in Basel is standing?: ")
if Answer4.lower() == "marktplatz":
    print("Someone knows their way around Basel, congrats!")
    count += 1
    if count == 4:
        print("You already have a 4 times streak - Just one more and you got 100% correct! ")
else :
    print("Go and Study the map of Basel a bit better, you should have known that!")
print("......... ")
# 5 #################################################################
Answer5 = input("5. How many people are living approximately on the planet earth? Give the numbers in billions (e.g. 1.2): ")
Answer5 = float(Answer5)
if Answer5 >= 7.5 and Answer5 <= 8.2:
    print("Last Question is right, you're a genius!")
    count += 1
    if count == 5:
        print("You got all your answers right. You're from another Planet! *_* ")
else :
    print("Oh noo, you missed that one - don't be too sad about it - it was a harder one :-( ")

result = count / 5 * 100
print("Let's look at your results, you got", result, "out of 100%")

