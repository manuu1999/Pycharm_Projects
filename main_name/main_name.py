# if you print __name__ it automatically prints __main__
print(__name__)
# it shows you were the code runs and main means that it runs directly in this file
if __name__ == '__main__':
    print("Code runs here ")
else:
    print("Code was imported")

