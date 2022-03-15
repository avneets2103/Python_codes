#tuples: nt updatable data type or non updatable list
#tuple is immutable
t=(1,2,3,5,6,3,5)
print(t) #dont prints the whole tuple here, but the mid value or mean
print(t[3])

#methods of tuples
a=t.count(5)
print(a)
print(t.index(2)) #tells index of first occuring of the element mentioned 
#t[2]=5 shows error
