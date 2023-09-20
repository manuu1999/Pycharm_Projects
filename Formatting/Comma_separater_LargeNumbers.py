# Separate large numbers
sentence = '1MB is equal to {:,} bytes'.format(1000**2)
print(sentence)
# Separate large numbers + add decimals
sentence = '1MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)


