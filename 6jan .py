#def factorial():
 #   num = int(input("Enter a number to find its factorial: "))
  #  fact = 1
   # for i in range(1, num + 1):
    #    fact = fact * i
    #print(f"The factorial of {num} is {fact}")
#factorial()

#def factorial(N):
 #   fact = 1
  #  for i in range(1, N + 1):
   #     fact = fact * i
    #return fact
#num = int(input("Enter a number to find its factorial: "))
#result = factorial(num)
#print(f"The factorial of {num} is {result}")

def factorial(N):
    print(f"computing factorial of {N}")
    if N == 1:
        return 1
    return N* factorial(N-1)
res = factorial(5)