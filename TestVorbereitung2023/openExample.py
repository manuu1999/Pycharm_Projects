try:
    with open('test.txt', 'r') as file:
        str = file.readlines()
        print(str)
except Exception as e:
    print(e)

for i in str:
    print(i)

