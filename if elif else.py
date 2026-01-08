num=eval(input('enter number: '))
if num==0:
    print("number is zero")
elif num>0:
    print(f"{num} number is positive")
else:
    print(f"{num} number is negative")

# To check who will pay the bill using if elif else
jay = 23
viru = 25
gabbar = 24
if jay>viru and jay>gabbar:
    print("jay will pay the bill")
elif viru>jay and viru>gabbar:
    print("viru will pay the bill")
else:
    print("gabbar will pay the bill")

jay = 23
viru = 23
gabbar = 23
if jay>viru and jay>gabbar:
    print("jay will pay the bill")
elif viru>jay and viru>gabbar: