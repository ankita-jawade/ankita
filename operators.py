#a = [1,2,3,4]
#b = [1,2,3,4]
#c = a 
#print(id(a))
#print(id(b))
#print(id(c))
#print(a is b)
#print(a is c)
#print(a == b)
n =1432
n1 = n//10   # to remove last digit
print(n1)
n2 = n1%10     # get last digit
print(n2)
n3 = n2//10     # remove last digit
print(n3)

    # find the total number of digits in a number

num = 12345
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Total number of digits:", count)

        # Arithmetic operators
a = 99
b = 10
print(a + b)
print(a - b)
print(a * b)

a = 45
c = "four"
print(a + c)
print(a - c)  # it will give error unsupported operand
print(a * c)  # it will give error unsupported operand
print(a / c)  # it will give error unsupported operand

            # take two list 
l = [43,45,56,78]
m = [12,34,45,67]
print(l + m)
print(l * 2)       # it will repeat the list two times
print(l - m)       # unsupported operand
print(l / m)       # unsupported operand

            # take two string
s1 = "hello "
s2 = "world"
print(s1 + s2)

            # take one list and one string
s = [22,12,12,34,54]
l1 = "money"
print(s + l1)    # it will give error unsupported operand 
print(s * l1)
print(s - l1)
print(s% l)
print(s / l)
print(s // l)     # it will give error unsupported operand

              # take both are tuple

t1 = (12,34,45,56)
t2 = (67,78,89,90)
print(t1 + t2)      # o/p will be concatenation of both tuple
print(t1 * t2)       # can't multiply two tuple by non-integer of type 'tuple'
print(t1 - t2)      # unsupported operand
print(t1 / t2)      # unsupported operand

            # take both are set

s1 = {89,90,78}
s2 = {12,34,45,90}
print(s1 + s2)      # unsupported operand
print(s1 * s2)      # unsupported operand      
print(s1 - s2)      # it will give difference of two set {89,78}
print(s2 - s1)    # it will give difference of two set {12,34,45}
print(s1 / s2)     # unsupported operand

    # take one integer value and one list

a = 45
l = [12,34,45,56]
print(a + l)     # unsupported operand
print(a - l)     # unsupported operand
print(a * l)     # it will repeat the list 45 times

            # take one string and one tuple
s = "being smart "
t = (12,34,45)
print(s + t)     # unsupported operand
print(s - t)     # unsupported operand
print(s * t)     # can't multiply sequence by non-int of type 'tuple'