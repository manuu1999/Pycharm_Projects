for i in range(1,4):
    sentence = 'The value is {0}'.format(i)
    print(sentence)
# formatted output new 02 instead of 2:
print("And now differently formatted: ")
for i in range(1,4):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)

