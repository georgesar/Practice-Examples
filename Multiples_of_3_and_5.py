l = []
for i in range(1, 1000):
    if i % 3 == 0:
        l.append(i)
    elif i % 5 == 0:
        l.append(i)

print sum(l)
