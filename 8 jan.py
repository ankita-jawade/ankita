#list_marks = [1,2,3,4,5,6,7,8]
#grace_marks = list(map(lambda x: x + 5, list_marks))
#print(grace_marks)
#grace_marks = list(filter(lambda x: x+5, list_marks))
#print(grace_marks)
#test_marks = [16.17,90,78,98]
#from functools import reduce
#max = reduce(lambda a,b: a if a > b else b, test_marks)
#print(max)
def displayname():
    print("ankita")

def mydecoration(func):
    def wrapper():
        print("good morning")
        print("*"*10)
        func()
        print("*"*10)
        print("Bye Bye")
    return wrapper
displayname = mydecoration(displayname)
displayname()