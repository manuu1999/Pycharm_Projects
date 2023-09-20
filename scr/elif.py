# Das Schlusselwort "elif" ist eine
# Kurzform fur ein "if" nach einem "else"
# Es ermöglicht uns, mehrere Boolesche Ausdrucke ohne Verschachtelungen zu überprüfen
# Wenn die Boolesche Bedingung in der if-Klausel falsch ist, wird die
# Bedingung des nächsten elif-Blocks überprüft
# Ist die Bedingung hier auch falsch, wird der nächste elif-Block überprüft, und so weiter.
# Wenn alle Booleschen Bedingungen falsch sind, werden die Anweisungen unterhalb vom else ausgeführt
# (der "else" Block ist dabei optional)

number = input("type in a number ")
number = int(number)
if number % 3 == 0:
    print("you can divide the number by 3")
elif number % 4 == 0:
    print("you can divide the number by 4 ")
elif number % 5 == 0:
    print("you can divide the number by 5")
