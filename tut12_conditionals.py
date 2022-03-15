#conditionals in pyhton
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))

#if-else-elif ladder
if (a>b):
    print(a," is larger than ",b)
elif(a==b):
    print(a," ",b," are equal")
else:
    print(a," is smaller than ",b)

#multiple-if
if(a>b):
    print("1")
if(a/2>b):
    print("2")

#None is also a data type in python

#  in is also a operator
a=[1,2,4,54,657]
if 54 in a:
    print("true")
    
