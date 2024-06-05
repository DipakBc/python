# Strings Slicing and Operations in strings ...

names = "Deepak,Nabin"
print(names[0:6])   # 0 to n-1 
print(len(names)) # to find length of strings we use len() function.

fruit = "mango"
print(len(fruit))
# print(fruit[0:4]) or print(fruit[:4]) do same 

print(fruit[0:-3]) # Negative slicing 
print(fruit[0:len(fruit) - 3]) #both do same 
'''
- 3 or len(variable) - 3 is same  
[-3:-1] or [len(var) -3 : len(var) -1 ]

0-4 including 0 but not 4
5-9 including 5 but not 9

'''


#quiz : name = "Harry" and print(namme[-4:-2])
name = "Harry" 
print(name[-4:-2])