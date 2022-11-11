# This is a little test on how to play around with the diffrent typs of data.
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# Getting into how lists work.  How to bild them, and how to play with them.
# This is ment to have an error in it.  I'll fixt it for now.
mylist = [1,2,3]
print(mylist[2]) # I had asked for the tenth position, but it would error and be a pain.

# This is a test I found.

numbers =[]
strings =[]
names =["John", "Eric", "Jessica"]

# This is where I will write my own code.

numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("Hello")
strings.append("World")
second_name = None

#this is the part that checkes the code.
print(numbers)
print(strings)
print("The second name on the names list is %s")

# onto more Maths.

# Basic Operators

number = 1 + 2 * 3 /4.0
print(number)

remainder = 11 % 3
print(remainder)

# Two multiplications symbols make a power relationship.
# It also looks like I don't need to have the extra spaces in the code,
# But it does look like it makes the code a little eaiser to read.

squared = 7 **2
cubed = 2**3
print(squared)
print(cubed)

# Now I will try to use operations with Strings.

helloworld = "hello" + " " + "world"
print(helloworld)

# This looks like I can add strings to the end of other strings with the +.

# looking ahead, this one looks cool.  I can multiply a string to form a repeating
# sequence.

lotsofhellos = "hello" * 10
print(lotsofhellos)
 # That one is fun.

 # Using Operations with Lists; how to add lists together with addition operators.

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# This one is nice, but it only puts one list on the end of the other list.
# I thought I could sort the list. A quick search looks like sorted is the tool.

all_numbers_sorted = sorted(all_numbers)
print(all_numbers_sorted)

# I struggled with how to get that to work, but I found if I make a new variable,
# I could sort all_numbers and print the new variable.

# Here is another test-ie-boi

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")