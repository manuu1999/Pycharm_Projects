# 1. Slicing
s1 = 'Manuel'
s1 = s1[1:4]
# Returns substring
# First one included/last one excluded
print("s1: ", s1)

# 2. Strip
s21 = '    hello you   '.strip()
#returns without spaces beginning and end
print("s21: ", s21)
s22 =  '###hello you###'.strip('#')
print("s22: ", s22)

# 3. remove prefix
s3 = 'Arthur: three!'.removeprefix('Arthur')
print("s3: ",s3)

# 4. remove suffix
s4 = 'Arthur: three!'.removesuffix('three!')
print("s4: ",s4)

# 5. replace
s51 = 'String Methods in Python'.replace(' ', '-')
print("s51", s51)
s52 = 'String Methods in Python'.replace(' ', '')
print("s52", s52)

# 6. split
s61 = 'String Methods in Python'.split()
print("s61: ", s61)
s62 = 'String,Methods,in,Python'.split(',')
print("s62: ", s62)

# 7. Join
list_of_strings = ['String', 'Methods', 'in', 'Python'];
s7 = '-'.join(list_of_strings)
print("s7: ", s7)

# 8. Upper
s8 = 'python is awesome!'.upper()
print("s8: ", s8)

# 9. Lower
s9 = 'PYTHON IS AWESOME'.lower()
print("s9: ", s9)

# 10. capitalize
s10 = 'python is awesome'.capitalize()
# only first letter gets capitalized
print("s10: ", s10)

# 11. count
s11 = 'hello world'.count('o')
print("s11: ", s11)

# 12. startswith / endswith
s121 = 'Patrick'.startswith('P')
print("s121: ", s121)
s122 = 'Patrick'.endswith('ck')
print("s122", s122)

# 13. center, ljust, rjust
s131 = 'Manuel'.center(20, '-')
# if you want a String with a
# certain length (fills up
# with what you give)
print("s131: ", s131)
s132 = 'Manuel'.ljust(20, '-')
print("s131: ", s132)
s133 = 'Manuel'.rjust(20, '-')
print("s131: ", s133)

# 14. f-Strings
num, language = 10, 'Python'
s14 = f'{language} has {num * 3 + 1} essential String methods'
print("s14: ", s14)







