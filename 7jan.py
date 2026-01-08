#test_marks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#grace_marks = []
#for i in test_marks:
 #   grace_marks.append(i + 2)
#print(grace_marks)

#def addfive(n1):
 #   return n1 + 2
#for i in test_marks:
 #   m = addfive(i)
  #  grace_marks.append(m)
#print(grace_marks)

#new_grace_marks = list(map(addfive, test_marks))
#print(new_grace_marks)


#tooper_marks =[]
#def topper(marks):
 #   return marks >85
#topper_marks = list(filter(topper, list_marks))
#print(topper_marks)
#def addtwo(a,b):
 #   return a + b
#from functools import reduce
#add = reduce(addtwo , list_marks)
#print(add)
list_marks = [67,87,5,89,95,65]
#def my_max(a,b):
 #   if a > b:
  #      return a
   # else:
    #    return b
#from functools import reduce
#maximum = reduce(my_max, list_marks)
#print(maximum)

def second_max(nums):
    if not nums:
        raise ValueError("Empty list")
    max1 = max2 = float('-inf')
    for x in nums:
        if x > max1:
            max2, max1 = max1, x
        elif max1 > x > max2:
            max2 = x
    if max2 == float('-inf'):
        raise ValueError("Need at least two distinct values")
    return max2
from functools import reduce
result = second_max(second_max, list_marks)
print(result)
