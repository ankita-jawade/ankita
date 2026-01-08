def addtwo(a,b):
    return a + b
def my_decorator(func):
    def wrapperfunc(a,b,c):
        res = func(a,b)
        res2 = res + c
        return res2
    return wrapperfunc
@my_decorator
def add(a,b):
    return a + b
result = add(2,3,5)
print(result)