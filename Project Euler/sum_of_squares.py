l = []
g = []
i = 1
while i <= 100:
    l.append(i ** 2)
    g.append(i)
    i += 1

print (sum(g) ** 2) - sum(l)


