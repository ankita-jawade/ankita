#n1=10.3
#n2=5.9
#sum=n1+n2
#print('sum of %f and %f is %f'%(n1,n2,sum))

#print('sum of %0.2f and %0.2f is %0.1f'%(n1,n2,sum))

#movies=[]
#movies.append(input('enter 1st mov: '))
#movies.append(input('enter 2nd mov: '))
#movies.append(input('enter 3rd mov: '))
#print(movies)

l=[11,22,33,44,11,55,66,77,44,77,66]
l.index(11)
print(l.index(11))
print(l.index(11,3))
print(l.index(33))
print(l.index(77,7))
print(l.index(77,8))
print(l.index(66,7,11))
l.reverse()
print(l)
