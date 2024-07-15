# In this we will see how to assign multiple variables their respective input value.

# Input is taken by input(), this gives a string.
# To take integer input we use typecasting like int(),float(),etc.


# This shows that input is string

vale=[]
vale= input("write list")
print(type(vale))
print(vale)

# using split method by space we use input in our desired type

vale_2=[]
vale_2= input("write list").split()
print(type(vale_2))
print(vale_2)


#####################
# so in cp when input is integer with space 
#  we use split and map to type cast it

input_string=input()  # type(input_string) will be string
a,b,c,d=map(int,input_string.split()) #split() method is seperating strings by space, map is typecasting those to integer.

# if we not typecast them then a,b,c,d we will be string.

#####################
