# In python you can perform any operation withou using any variable
print(2*3)
print(2+3)
print(3/2)
print(3-2)

print('---------------------------------------n/')
# you can use variable to make it simple
print('operations Using variable')
x = 2; y = 3

print(x*y)
print(x+y)
print(x/y)
print(x-y)
print('---------------------------------------n/')
# By how many ways we can print string and variable in print function
print('you can print string and variable using concatenation and using format string')
print('the addition between',x,'and',y,'is',x+y)
# using format string
print(f"the addition between {x} and {y} is {x+y}")
#Some example of format string like print in same line and print next line in same print function
print(f"the addition of {x} and {y} is {x + y} and "
      f"the multiplication of {x} and {y} is {x * y}")
# for next line
print(f"the addition of {x} and {y} is {x + y} and \nthe "
      f"multiplication of {x} and {y} is {x * y}")
print('---------------------------------------n/')

# Assignment 1 - calculate total profit for two goods

goods1_cp = 12
goods1_sp = 20
goods1_qty = 200
goods2_cp = 20
goods2_sp = 40
goods2_qty = 150
profit_goods1 = (goods1_sp - goods1_cp)*goods1_qty
print(f"the profit on goods1 is {profit_goods1}")

profit_goods2 = (goods2_sp - goods2_cp)*goods2_qty
print(f"the profit on goods2 is {profit_goods2}")

total_profit = profit_goods1+profit_goods2
print(f"total profit {total_profit}")
print('---------------------------------------n/')

# Assignment 2 - WAP to take length and breadth of rectangle and display its area and perimeter in output
length = 2
width = 3

area = length * width
perimeter = 2*(length) + 2*(width)

print('the area of rectangle is',area)
print('the perimeter of rectangle is',perimeter)
print('---------------------------------------n/')

# Assignment 3 - WAP to take radius and calculate are and circumference of circle
radius = 3

circumference = 2 * 3.14 * radius
area = 3.14 * radius * radius

print('area of circle is',area)
print('circumference of circle  is',circumference)

