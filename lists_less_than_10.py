a = [2, 6, 8, 4, 56, 54, 5, 5, 6, 7, 7, 6, 534, 4, 324, 12]
b = []
for i in a:
    if i < 5:
        print i
        b.append(i)

print b

q = raw_input('Please enter a number: ')
c = []
for new_var in a:
    if new_var < int(q):
        c.append(new_var)
print c