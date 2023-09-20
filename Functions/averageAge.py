def stud_av_age():
    # attention: list is on purpose initialized outside the while loop
    li = []
    while True:
        age = int(input("Neues alter für ein neuen Student hinzufügen (oder 0 eingeben um zu stoppen): "))
        if age == 0:
            amount = 0
            for i in li:
                amount += i
            print(amount)
            average = amount / len(li)
            print("Durchschnittsalter ist: ", average)
            break
        else:
            li.append(age)
            print(li)

stud_av_age()

