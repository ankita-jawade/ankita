#student_db = {1 : "monu", 2 : "priya", 3 : "meera"}
#print(student_db.items())

mi = {45 :"rohit sharma", 11 :"sachin tendulkar", 7 :"rahul dravid",63 : "surya kumar"}
#print("total player of mi team =",len(mi))
#print(mi.keys())
#for k in mi.keys():
    #print("player no =",k)
#for i in mi:
 #   print(
count =0 
for jn in mi:
    if "y" in mi[jn]:
        print(mi[jn])
        count = count+1
print("total player having y in their name =",count)    

count =0
for j in mi:
    if len(mi[j])>12:
        print(mi[j])
        count = count+1
print("total player having name length greater than 12 =",count)

for j in mi:
    if mi[j].endswith("a"):
        for ch in mi[j]:
print(ch)
    


