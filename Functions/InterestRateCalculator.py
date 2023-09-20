def calc ():
    amount = input("What's the amount your investing? ")
    amount = float(amount)
    duration = input("How long do you want to invest? ")
    duration = int(duration)
    rate = input("How much interest do you get? ")
    # 4.5 zins it shows it like 1.045, for calculation below
    rate = (float(rate))/100 + 1
    # profit = 100 * 1.045^5
    profit = amount * rate**duration
    print("Amount: ", amount)
    print("Interest rate in percentage: ", rate.__format__(".2f"))
    print("Duration in years: ", duration)
    print("Expected profit: ", profit.__format__(".2f"))

calc()
