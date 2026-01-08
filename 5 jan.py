#def sign_up(cn="tcs",age=24,sal=25000,en='meena'):
    #print(f"Employee name is {en}")
    #print(f"Employee age is {age}")
    #print(f"Employee salary is {sal}")
    #print(f"Employee company name is {cn}")
#sign_up("Ankita",22)
#sign_up("tcs",25,25000,"meena")

#def add(*args):
    #print(args)
    #print(type(args))
    #sum=0
    #for i in args:
     #   sum=sum+i
    #return sum
#result=add(10,23,45,7,56,87,0,21)
#print(result)

def submit(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k,"--->",v)
        print(k[0],v[0])
submit(name="Ankita",age=22,sal=25000,cn="tcs")