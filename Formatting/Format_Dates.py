# year,month,date,hours,minutes,seconds
import datetime
my_Date = datetime.datetime(2016,9,24,12,30,45)
print(my_Date)

# Format month, day, year
sentence = '{:%B %d, %Y}'.format(my_Date)
print(sentence)

