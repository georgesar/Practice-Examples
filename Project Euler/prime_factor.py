l = []
i = 2
number = int(600851475143)

while i <= number:
    if number % i == 0:
        l.append(i)
        number = number / i
    i += 1

print max(l)
