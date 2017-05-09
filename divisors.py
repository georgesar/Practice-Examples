num = int(raw_input('Please enter a number: '))
li = range(1, num + 1)
new_li = []
for i in li:
    if num % int(i) == 0:
        new_li.append(i)

print new_li

