# check numbers is divisible by 3 using lambda function 

numbers = [2,12,5,78,36,48,9]
print(list(filter(lambda num : num%3==0,numbers)))  # [12,78,36,48,9]

# calculate square of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda num : num**2,numbers)))   # [1,4,9,16,25,36,49,64,81,100]

print(dict(map(lambda num:(num, num**2),numbers))) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# convert list of studentas in upper case
students = ['meera','jaya', 'niyu','teetu','monu','ankita','pankaj',]
print(list(map(lambda name: name.upper(),students))) #['MEERA', 'JAYA', 'NIYU', 'TEETU', 'MONU', 'ANKITA', 'PANKAJ']

# calculate length of students take output as dictionary

print(dict(map(lambda name : (name,len(name)),students)))  #{'meera': 5, 'jaya': 4, 'niyu': 4, 'teetu': 5, 'monu': 4, 'ankita': 6, 'pankaj': 6}

l = [4,8,12,16,30,24]
num = list(filter(lambda x:x%3==0 and x%4==0,l))
print(num)   #[12, 24]