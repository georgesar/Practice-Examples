number = raw_input('Please enter a number: ')

while number != 'exit':
    while not number.isdigit():
        number = raw_input('Please give a number this time... :')

    while int(number) == 0:
        print 'Number is zero'
        number = raw_input('Please enter a number: ')
    else:
        if int(number) % 4 == 0:
            print'Number is a multiple of 4'
        elif int(number) % 2 == 0:
            print 'Number is even'
        else:
            print 'Number is odd'
    break

cont = raw_input('Do you want to play another game? y/n ').lower()

if cont == 'n':
    print 'Goodbye'

elif cont == 'y':
    num = raw_input('Please enter a number: ')
    check = raw_input('Please enter another number to divide ' + num + ' by: ')
    if int(check) % int(num) == 0:
        print check + ' divides evenly in ' + num +'!'
    else:
        print check + ' does not divide evenly in ' + num

