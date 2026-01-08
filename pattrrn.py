#for rows in range(5+1,1,-1):
    #for cols in range(1,rows):
    #    print('*',end=' ')
   # print()
#N=5
#for i in range(N,N+1):
 #   print("*"*i)
#for rows in range(1,N+1):
 #   for cols in range(1,rows+1):
  #      print(cols,end=' ')
   # print()
#wap to pattern for right angle triangle 
#def pattern(n):
 #   for rows in range(1,n+1):
  #      for cols in range(1,rows+1):
   #         print('64+cols',end=' ')
    #    print()
#pattern(5)

def pyramid(n):
    """Print a centered pyramid of stars with n rows."""
    for i in range(1, n+1):
        # left padding + repeated "* " pattern
        print(' ' * (n - i) + '* ' * i)