#def outerfun(x):
    #print(x)

    #def innerfun():
     #   print("This is inner function")
      #  print(x)
    #print("Calling inner function")
    #inner

def outerfun(a):
    def innerfun(b):
        return a + b
    return innerfun
addtwo = outerfun(2)
res = addtwo(5)
print(res)
addtwo1 = outerfun(10)
res1 = addtwo1(5)
print(res1)