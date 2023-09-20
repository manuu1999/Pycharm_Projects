def my_function(num):
    if num%3 == 0:
        if num % 3 == 0 and num % 5 == 0:
            print("BizzBuzz")
        else: print("Bizz")
    elif num%5 == 0:
        if num % 3 == 0 and num % 5 == 0:
            print("BizzBuzz")
        else: print("Buzz")
    else:
        print(num)

for i in range(1,100):
    my_function(i)

