#sets in python
# remove repetition from it
#syntax: 
# set_name = {e1,e2,e3,....,eN} if any element repeats it will ignore it

a={} #creates empty dict nt an empty set
print(type(a))
#for empty set
b=set()
b.add(986)
b.add(4)
print(type(b))
print(b)

c={1,3,5,7,9,2,2}  #sort and repetition remove
print(c)

myDict={
    "harry":"coder",
    "hello":"pyhton"
}

#set_methods
c.add(4)
c.add(6)
c.add(6) #wont matter if added twice
print(c)
#c.add([2,3,4,5]) #throws error as list cant be added to set as list is immutabe
c.add((2,5,7,84,43))
#c.add({myDict}) #throws wrror as dict cant be added to set as it is immutable
print(c)
print(len(c)) #prints the length of set
c.remove(2) #removes the element with value 5
print(c)
print(c.pop()) #remove random element of the set and prints the element
print(c)
c.clear()
print(c)
c.add(4)
c.add(6)

d=c
#union,intersection
c.union({986,4})
print(c)
d.intersection({986,4})
print(d)

