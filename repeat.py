num1=eval(input('enter num1: '))
opr=input("enter operator: ")
num2=eval(input("enter num2: "))
if opr=="+":
    print(f"sum of two number : {num1+num2}")
elif opr=="-":
    print(f"substraction of two number : {num1-num2}")
elif opr=="*":
    print(f"multiplication of two number : {num1*num2} ")
elif opr=="/":
    print(f"division of two numbers :{num1/num2}")
else:
    print("invalid operator")