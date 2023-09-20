import random

Li = ["Rock", "Scissor", "Paper"]

print("Hello and welcome to my rock, scissor, paper game - let's start playing ")
count = 0
while True:
    print("Your count is: ", count)
    ran = random.choice(Li)
    ans = input('Rock, Scissor or Paper? (type "quit" if you want to leave the game)')
    if ans == "quit":
        break
    elif ran == "Scissor" and ans == "Scissor":
        print("Your opponent has ", ran, "and you took ", ans)
        print(".... No point for anyone this round")
        continue
    elif ran == "Rock" and ans == "Scissor":
        print("Your opponent has ", ran, "and you took ", ans)
        print(".... Your opponent won this time - next try ")
        count -= 1
        continue
    elif ran == "Paper" and ans == "Scissor":
        print("Your opponent has ", ran, "and you took ", ans)
        print(".... You won this round - congrats! ")
        count += 1
        continue
     ######################################################
    elif ran == "Scissor" and ans == "Rock":
        print("Your opponent has ", ran, "and you took ", ans)
        print(".... You won this round - congrats! ")
        count += 1
        continue
    elif ran == "Rock" and ans == "Rock":
        print("Your opponent has ", ran, "and you took ", ans)
        print(".... No point for anyone this round")
        continue
    elif ran == "Paper" and ans == "Rock":
        print("Your opponent has ", ran, "and you took ", ans)
        print(".... Your opponent won this time - next try ")
        count -= 1
        continue
    #######################################################
    elif ran == "Scissor" and ans == "Paper":
        print("Your opponent has ", ran, "and you took ", ans)
        print(".... Your opponent won this time - next try ")
        count -= 1
        continue
    elif ran == "Rock" and ans == "Paper":
        print("Your opponent has ", ran, "and you took ", ans)
        print(".... You won this round - congrats! ")
        count += 1
        continue
    elif ran == "Paper" and ans == "Paper":
        print("Your opponent has ", ran, "and you took ", ans)
        print(".... No point for anyone this round")
        continue
