i = 100
j = 100
c = 0
g = []
f = []
while 10 <= i <= 999:
    while 10 <= j <= 999:
        c = j * i
        g.append(c)
        j += 1
    j = 100
    i += 1

for item in g:
    if str(item) == str(item)[::-1]:
        f.append(item)

print max(f)
