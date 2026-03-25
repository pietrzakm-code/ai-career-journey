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