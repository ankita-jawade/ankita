#sum = lambda x,y : x+y
#print(sum(10,20))
 
#square=lambda num : num**2
#print(square(3))

#students ={"kunal":89, "om":78, "raj":32, "kiran":21, "atul":89,"pradep":31, "rajesh":22, "bhushan":90 ,"vaibhav":34, "karan":99}
#print(list(filter(lambda name : students[name]>= 40,students)))
#print(dict(filter(lambda t : t[1]>=40,students.items())))
#nm = [name for name in students if name.startswith('k')]
#print(nm)
#nm = [name for name in students if students[name]>= 40]
#print(nm)
#l = [name.upper() if students[name]>=40 else name.lower() for name in students ]
#print(l)

#numbers = [1,2,3,4,5,6,7,8,9,10]
#sc = [ num**2 if num%2==0 else num**3 for num in numbers]
#print(sc)

#sentence = "hello world"
#unique_char = [ char for char in sentence if char != '']
#chars = {ch for ch in sentence}
#print(chars)
#vowels = {ch for ch in "education " if ch in "aeiou"}
#print(vowels)
product_mrp=["laptop":50000,"mbl":20000,"speker":10000,"tv":30000]
product_sp=[product:mrp-mrp*10/100 for product,mrp in product_mrp.items()]
print(product_sp)
