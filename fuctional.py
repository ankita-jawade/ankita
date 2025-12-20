#def square():
    #num=eval(input("enter number: "))
    #sq=num**2
    #print(sq)
#def cube():
    #num1=eval(input("enter number: "))
    #cu=num1**3
    #print(cu)

#def even():
    #num=eval(input('enter number: '))
    #if num%2==0:
       # print(f"{num} is even number")
    #else:
        #print(f"{num} is odd number")
#even()

def count_length():
    word=input("enter word: ")
    char=input('enter char: ')
    count=0
    for i in word:
        if char==i :
            count=count+1
    print(count)
count_length()