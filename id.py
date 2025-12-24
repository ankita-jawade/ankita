#a  = [1,3,4,5]
#print(id(a))
#accept two numbers from console using input function and check their output
#a = int(input("enter first number: "))
#b = int(input("enter second number: "))
#print("id of a:", id(a))
#print("id of b:", id(b))
#print("a is b:", a is b)

#s1 = input("enter first string: hello world ")
#s2 = input("enter second string: meena")
#print(s1 in s2)
l = ["python","java","c++","ruby","perl"]
#print("python" in l)
#print("go" not in l)
#print  character in each string present in the list
for item in l:
    for char in item:
        print(char)
print("a" in "java")
print("y" not in "ruby")
print("z" in "c++")
print("x" not in "perl")



