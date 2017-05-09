print bin(1024)
print hex(1024)

print round(5.2322, 2)

s = 'hello how are you Mary, are you feeling okay?'
d = s.translate(None, ' ,?')
b = len(d)
c = 0
for i in s:
    if i.isalpha():
        c += 1
    else:
        break
if b == c:
    print 'All lowercase'
else:
    print 'Not all lowercase'


j = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'

print j.count('w')

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print set1.difference(set2)

print set1.union(set2)

dict = {x:x**3 for x in range(5)}
print dict

l1 = [1,2,3,4]
l1.reverse()
print l1

l2 = [3,4,2,5,1]
l2.sort()
print l2