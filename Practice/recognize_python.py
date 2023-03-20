num1 = 42   # variable declaration, number
num2 = 2.3  # variable declaration, floating point number or decimal 
boolean = True  # vairable  declaration, boolean
string = 'Hello World'  # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #variable declaration, dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuple
print(type(fruit))  # print to console, type check
print(pizza_toppings[1])    # print to console, list  access value 
pizza_toppings.append('Mushrooms')  # list add value
print(person['name'])   # print to console, dictionary access value
person['name'] = 'George'   # dictonary, change value
person['eye_color'] = 'blue'    # dictonary, change value 
print(fruit[2]) #print to console, tuple access value

if num1 > 45:
    print("It's greater")
        
else:
    print("It's lower")
# conditional if, print to console, conditional else, print to console

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# conditional if, print to console, conditional else if, print to console, conditional else, print to console 

for x in range(5):
    print(x)
# for loop, start at 0, end at 5
for x in range(2,5):
    print(x)
# for loop, start at 2, end at 5
for x in range(2,10,3):
    print(x)
# for loop, start at 2, end at 10 ,increment by 3
x = 0   # while loop, variable declaration
while(x < 5):
    print(x)    # print t console
    x += 1  # increment x by 1

pizza_toppings.pop()    # list delete value, at end
pizza_toppings.pop(1)   # list delete value,  at index 

print(person) # print to console, dictionary
person.pop('eye_color') # dictonary, delete value 
print(person)   # print to console, dictionary

for topping in pizza_toppings: # for loop, list
    if topping == 'Pepperoni':  # conditional if
        continue    # continue 
    print('After 1st if statement') # print to console 
    if topping == 'Olives': # conditional if 
        break # loop end 

def print_hello_ten_times():    # function declaration 
    for num in range(10):   # for loop, start at 0, end at 10 
        print('Hello')  # print to console 

print_hello_ten_times() # function delcation 

def print_hello_x_times(x):
    for num in range(x): # for loop, until x 
        print('Hello')  # print to console 

print_hello_x_times(4)  

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):    # for loop until x 
        print('Hello')  # print to console 

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)