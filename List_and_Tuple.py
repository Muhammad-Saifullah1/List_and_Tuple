# List

my_list = [10, 20, 30, 40]
print(my_list)

#Indexing in list

print(my_list[0]) 
print(my_list[-1])

#changing element 

my_list[2]="Saifullah"
print(my_list)

#Methods

my_list.append(45)
print(my_list)

my_list.insert(2,"100")
print(my_list)

my_list.remove(45)
print(my_list)

my_list.pop(2)
print(my_list)

#Slicing 
print(my_list[1:3])

#TUPLE

my_typle = (10,20,30)
print(my_typle)

# Indexing
print(my_typle[2])

# Cannot change
# my_typle[2]=45 ------->Give error

# Methods
t = (1,2,2,2,3,3,3,3,3,3,3,3,4,5,6)
print(t.count(3))

print(t.index(4))