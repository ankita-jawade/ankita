#num = int{ input('enter a number: ')}
#if num % 3 == 0 and num % 5 == 0:
 #   print{"FIZZBUZZ"}
#elif num % 5 == 0:
 #   print{"BUZZ"}
#elif num % 3 == 0:
 #   print('FIZZ')
#else:
    #print{'number is not divisible by 3 and 5'}

# wap to display  100 t0 10 numbers using for loop
#for i in range(100, 9, -1):
 #   print(i)

#for i in range(100,9,-1):
 #   print(110-i)

numbers = []
for i in range(100,9,-1):
    numbers.append(i)
for n in reversed(numbers):
    print(n)
    