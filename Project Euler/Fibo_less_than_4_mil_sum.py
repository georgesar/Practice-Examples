l = []
g = []
a = 1
b = 0
while a <= 4000000:
    l.append(a)
    c = a + b
    b = a
    a = c

print l

for i in l:
    if i % 2 != 0:
        g.append(i)

print g
print sum(g)
