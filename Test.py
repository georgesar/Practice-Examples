import datetime

name = str(raw_input('Please enter your name: '))


year_today = datetime.datetime.now()

while not name.isalpha():
    print 'Please no not enter special characters or numbers for your name'
    name = raw_input('Please enter your name: ')

age = raw_input('Please enter your age: ')
while not age.isdigit():
    print 'Please enter numbers only'
    age = raw_input('Please enter your age: ')
else:
    years = 100 - int(age)
    when100 = year_today.year + years
    print 'Hello, %s, you will be 100 years old in year %s' % (name, when100)

rep = int(raw_input('Please enter a number: '))
i = 0
while i <= rep:
    print 'Hello, %s, you will be 100 years old in year %s' % (name, when100)
    i += 1



