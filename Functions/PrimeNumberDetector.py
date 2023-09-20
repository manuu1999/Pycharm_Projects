def is_prime():
    while True:
        n = int(input("Ganze Zahl eingeben, -1 zum Beenden: "))
        if n == -1:
            break
        else:
            for i in range(2, n):
                if (n % i) == 0:
                    print("Not a prime")
                    break
                else:
                    print("Prime")
                    break
is_prime()


