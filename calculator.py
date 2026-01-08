def avg():
    n1=int(input("Enter first number: "))
    n2=int(input("Enter second number: "))
    n3=int(input("Enter third number: "))
    average = (n1 + n2 + n3) / 3
    print("The average of three numbers is:", average)
avg()

def discount():
    result = avg()*5/100
    print("The discount is:", result)
discount()
