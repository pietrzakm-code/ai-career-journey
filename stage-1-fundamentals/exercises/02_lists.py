#This file is just to learn variables and operations 
#Not a good example of programming
#No file should look like that


# --- LIST ----------

#create a list
my_list = ["bmw", "honda", "ford"]

print(my_list)

#allow duplicates
my_list = ["bmw", "honda", "bmw", "ford"]

print(my_list)

#index
print(my_list[1])
print(my_list[-1])

#list length
print(len(my_list))

#list data types
my_list_bool = [True, True, False]
my_list_float = [1.0, 2.0, 3.0]
my_list_mix = ["George", "Novak", 46, True, 178.6]

#list type
print(type(my_list))

#constructor
my_list = list(("bmw", "ford", "toyota"))
print(my_list)

#check exist
if 'ford' in my_list:
    print("Yes, 'ford' is in the list")
if 'honda' not in my_list:
    print("No, 'honda' is not in the list")

#change item
my_list[1] = 'dodge'
print(my_list)

#add items to list
my_list.append('ford')
my_list.append('fiat')
my_list.append('honda')
print(my_list)

#change range of items
my_list[1:3] = ['jeep', 'nissan']
print(my_list)

#insert item
my_list.insert(3,'tata')
print(my_list)

#extend
my_list.extend(['seat', 'audi', 'porsche'])
my_list.extend(('kia', 'honda', 'toyota'))
print(my_list)

#remove
my_list.remove('tata')
print(my_list)

#remove at index
my_list.pop(-5)
del my_list[1]
print(my_list)

#clear list
my_list_tmp = list(my_list)
my_list_tmp.clear()
print(my_list_tmp)
print(type(my_list_tmp))


#delete list and variable
del my_list_tmp

#loop through list
for car in my_list:
    if car[0] == 'f':
        print(car)

#list comprehencion
[print(car, end=", ") for car in my_list]
print()

#list comprehension if
car_list = []
car_list = [car.upper() for car in my_list if car[1] == 'i']
print(car_list)

#sort
my_list.sort()
print(my_list)

numerical_list = [54, 82, 321, 0, -53, 45.7]
print(numerical_list)
numerical_list.sort()
print(numerical_list)

#sort descending
numerical_list.sort(reverse = True)
print(numerical_list)

my_list.sort(reverse = True)
print(my_list)

#sort customize
def my_func(n):
    return abs(n-40)

numerical_list.sort(key = my_func)
print(numerical_list)

#case sensitive
str_list = ['a', 'A', 'b', 'Z', 'i', 'h', "Me", 'urL']
str_list.sort()
print(str_list)
str_list.sort(key = str.lower)
print(str_list)

#reverse
str_list.reverse()
print(str_list)

#copy
car_list = my_list
print(car_list)
print(my_list)

my_list.append("subaru")
print(car_list)
print(my_list)

car_list = my_list.copy()
#! also a new list can be created by constructor x = list(lst) !
my_list.append("volvo")
print(car_list)
print(my_list)

#slice
car_list = my_list[5:]
my_list.append("mg")

print(car_list)
print(my_list)

#merge list
list1 = [1,2,3]
list2 = [4,5,6]

list_operator = list1 + list2
list_append = list1.copy()
for x in list2:
    list_append.append(x)
list_extend = list1.copy()
list_extend.extend(list2)

print(list_operator)
print(list_append)
print(list_extend)


# --- TUPLE ----------

#tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

#tuple is ordered, unchangeable, allow duplicate
my_tuple = ("apple", "banana", "apple", "cherry")
print(my_tuple)

#index
print(my_tuple[0], my_tuple[2])

#length
print(len(my_tuple))

#one item tuple
my_tuple = ("apple",)
print(my_tuple)

#tuple data types
my_tuple = ("apple", "cherry", "banana")
print(my_tuple)

my_tuple = ("apple", True, 3)

#tuple type
print(type(my_tuple))

#constructor
my_tuple = tuple(("apple", "cherry", "banana"))
print(my_tuple)

#change tuple - workaround
print(my_tuple)
my_list = list(my_tuple)
my_list.append("strawberry")
my_list.insert(1, "raspberry")
my_list.sort()
my_tuple = tuple(my_list)
print(my_tuple)

#unpack tuple
my_tuple = ("apple", "cherry", "banana")
(apple, cherry, banana) = my_tuple

print("{apple}, {cherry}, {banana}")

#unpack with less variables
my_tuple = ("apple", "cherry", "banana", "kiwi", "pinapple", "raspberry")
(apple, *cherry, banana) = my_tuple
print(apple)
print(cherry)
print(banana)

#loop
for x in my_tuple:
    print(x)

indx = 0
while indx < len(my_tuple):
    print(my_tuple[indx])
    indx += 1

#merge tuples
tuple2 = ("tomato", "potato", "carrot")
tuple3 = my_tuple + tuple2

print(tuple3)

#multiply
my_tuple = tuple3 * 2
print(my_tuple)


# --- SET ----------

#set
my_set = {"tomato", "potato", "carrot"}
print(my_set)

"""
sets are:
unordered
unchangeable (you can add and remove items from sets)
unindexed
don't allow duplicates
"""
#no duplicates
my_set = {"tomato", "potato", "carrot", "potato"}
print(my_set)

#1,0 and True,False are the same
print({1, 2, True, False, 0})

#length
print(len(my_set))

#set type
print(type(my_set))

#constructor
my_set = set(my_tuple)
print(my_set)

#get to set items
for x in my_set:
    print(x)

print("banana" in my_set)
print("bmw" in my_set)

#add item
my_set.add("pear")
print(my_set)

#add sets
fruits2 = ("orange", "grapefruit", "dragon fruit")
my_set.update(fruits2) # you can update set with any iterable

print(my_set)

#remove
my_set.remove("carrot") #will rise an error if "carrot" doesn'r exist
my_set.discard("tomato") #will NOT rise an error
#you can also .pop() - but will pop random item (tail)
print(my_set)

#union
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = {True, False, True}

print(set1.union(set2, set3)) #this way you can union other iterables
print(set1 | set2 | set3) #this way you can union only set with set

#intersection
print(set2.intersection(set3))
print(set2 & set3)

#intersection_update
set3.intersection_update(set2)
print(set3)

#difference
set3 = {0, 2, 4, 6}
set4 = {1, 2, 3, 5}

print(set3.difference(set4)) #also _update version
print(set3 - set4)

#symetric_difference
set3 = {0, 2, 4, 6}
set4 = {1, 2, 3, 5}

print(set3.symmetric_difference(set4)) #also _update version
print(set3 ^ set4)

#frozenset
x = frozenset(my_set)
print(x)
print(type(x))

#frozensets are immutable - can't mutate - no remove/add items