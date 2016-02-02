a = ('physics', 12,9,87,'mango','apple',71)
b = ('mango',21,12,34,71,'physics', 'chemistry')
l = [2,3,45,5,6,66]
print "First tuple length:",len(a)
print "First tuple length:",len(b)
print cmp(a, b)
print"Max value element:", max(a)
print"Max value element:", max(b)

print"Max value element:", min(a)

print"Max value element:", min(b)
tuple(l)
print l
l.sort()
print l
b.sort()
