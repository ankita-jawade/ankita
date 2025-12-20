def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def filter_prime(iterable):
    prime_numbers = []
    for num in iterable:
        isprime(num)
    else:
        return prime_numbers
print(filter_prime([2,3,7,6,5,9,]))