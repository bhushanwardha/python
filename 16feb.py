# we can decide the digit after decimal point
x = 123.1234
print(f"the number with 0 decimal digit {x:.0f}, with 1 decimal digit {x:.1f} and with 2 decimal digit {x:.2f}")
print('---------------------------------------n/')

# you can define multiple variable at once in single line
player, country, role = "Dhoni" , "India", "Captain"
print(f"The {player} plays for {country} as {role}")
print('---------------------------------------n/')

#you can format the sentence like table like structure
player, country, role = "Dhoni" , "India", "wicket-keeper"
print(f"The {player:<15} plays for {country:^15} as {role:>18} in a team")
player, country, role = "RickyPonting" , "Australia", "Captain"
print(f"The {player:<15} plays for {country:^15} as {role:>18} in a team")
#{player:<15} - 15 places allotted to variable player, < meaning in that 15 places dhoni is printed on left side
# if you don't give < , so default is left only
# instead of 15 you can give any number as you want as per formatting
# ^ sign meaning centre aligned and > meaning right aligned
# if you don't want blank spaces you just need to put whatever you want there just after :
print(f"The {player:.<15} plays for {country:-^15} as {role:_>18} in a team")
print('---------------------------------------n/')

#we have some data types in python -  int, string, float, complex, boolean
var1 = 5
print(type(var1))
var2 = -5
print(type(var2))
var3 = 2.5
print(type(var3))
var4 = -2.5
print(type(var4))
var5 = "python"
print(type(var5))
var6 = "True"
print(type(var6))
# in complex square root of -25 is 5j, square root of negative number is complex number
var7 = 5j
print(type(var7))
print(5j*5j)

var8 = True
print(type(var8))
var9 = False
print(type(var9))
var10 = "True"
print(type(var10))

print('---------------------------------------n/')

# arithmetic operatio  - "+", "-", "*", "/", "//","**","%"
var1 = 10
var2 = 3
print(var1 + var2)
print(var1 - var2)
print(var1 * var2)
print(var1 / var2)  # sign of normal division it gives actual result
print(var1 // var2) #sign of integer division it gives Quotient as result
print(var1 ** var2) # sign of power means 10^3
print(var1 % var2)  # sign of modulus , it gives remainder as a result

#------------------typecasting example------------------
# typecasting - converting one data type to another
# int to float
var1 = 5
var2 = 3
var3 = var1 / var2
print(var3)
var4 = float(var1) / float(var2)
print(var4)
# float to int
var5 = int(var3)
print(var5)
# int to string
var6 = str(var1)
print(var6)
# string to int
var7 = int(var6)
print(var7)
# string to float
var8 = float(var6)
print(var8)
# float to string
var9 = str(var8)
print(var9)
# string to boolean
var10 = bool("True")
print(var10)
# boolean to string
var11 = str(var10)
print(var11)


# WAP to decide how many of each currency notes are needed to make a given amount. Take amount value from user as input
# note: you have currency notes of 500, 100, 50, 20, 10, 5, 2, 1
# without using any loop
amount = int(input("enter amount \n"))
note_500 = amount // 500
amount = amount % 500
note_100 = amount // 100
amount = amount % 100
note_50 = amount // 50
amount = amount % 50
note_20 = amount // 20
amount = amount % 20
note_10 = amount // 10
amount = amount % 10
note_5 = amount // 5
amount = amount % 5
note_2 = amount // 2
amount = amount % 2
note_1 = amount // 1
amount = amount % 1
print(f"500 : {note_500}")
print(f"100 : {note_100}")
print(f"50 : {note_50}")
print(f"20 : {note_20}")
print(f"10 : {note_10}")
print(f"5 : {note_5}")
print(f"2 : {note_2}")
print(f"1 : {note_1}")


