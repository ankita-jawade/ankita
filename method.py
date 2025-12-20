#set1={'radha','meena', 'peena','leela', 'kavya', 'sheela'}
#set2={'jeeva', 'priya', 'peena', 'leela', 'killa', 'peela'}
#set3={'meena', 'leela','radha', 'heema', 'shila'}
#print(set1.intersection(set2,set3))
#print(set2.difference(set1))

s1 = {22,33,44,55,60,81.90}
s2 = {22,33,60,86,76,81}
l1 = {86,60, 99,90,45,56,33,60}
s2.symmetric_difference(s1)
print(s2)

s1.symmetric_difference(l1)
print(s1)
s1.intersection_update(l1)
s1.difference_update(s2)
s2.symmetric_difference_update(l1)
 