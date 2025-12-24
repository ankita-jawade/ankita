bollywood_2025 = {
    "Sikandar": ["Salman Khan", "Rashmika Mandanna"],
    "Housefull 5": ["Akshay Kumar", "Riteish Deshmukh", "Kriti Sanon"],
    "War 2": ["Hrithik Roshan", "Jr NTR", "Kiara Advani"],
    "Raid 2": ["Ajay Devgn", "Vaani Kapoor"],
    "Bhool Bhulaiyaa 3": ["Kartik Aaryan", "Triptii Dimri", "Vidya Balan"],
    "Welcome To The Jungle": ["Akshay Kumar", "Sanjay Dutt", "Disha Patani"],
    "Don 3": ["Ranveer Singh"],
    "Tehran": ["John Abraham", "Manushi Chhillar"]
}

print(bollywood_2025)
# print name of all movies from data base 
for movie in bollywood_2025.keys():
    print(movie)

print(bollywood_2025.keys())

# print number of cast in each movie

bollywood_2025 = {
    "Sikandar": ["Salman Khan", "Rashmika Mandanna"],
    "Housefull 5": ["Akshay Kumar", "Riteish Deshmukh", "Kriti Sanon"],
    "War 2": ["Hrithik Roshan", "Jr NTR", "Kiara Advani"],
    "Raid 2": ["Ajay Devgn", "Vaani Kapoor","Akshay kumar"]   
}
d_cast = bollywood_2025["Sikandar"]
h_cast = bollywood_2025["Housefull 5"]
w_cast = bollywood_2025["War 2"]
R_cast = bollywood_2025["Raid 2"]
print(len(d_cast))
for name,cast in bollywood_2025.items():
    print( name, 'total cast', {len(cast)})

# print name of movie which has akshay kumar in cast
count=0
for name,cast in bollywood_2025.items():
    if "Akshay Kumar" in cast:
        print('movie name with akshay kumar in cast:', name)
        count+=1
print('total movies with akshay kumar:', count)