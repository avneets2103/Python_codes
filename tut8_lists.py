#lists: Unline arrays uh can store diff data types in a list

a=[12.5,4,65,True,"hey"] 
print(a) #directly print the whole list
print(a[2])
a[4]="hello buddy"
print(a)

#slicing a list
#just exactly same as string
friends=["harry","avneet","akshi",45,65]
print(friends[1:4])
print(friends[-4:-2]) #and all other stuff same as string

#functions_of_list
l1=[2,3,56,234,5,23,65]
l1_sorted=l1.sort()#wrong method
l1.sort #its nt a returning function i.e. it make changes to the list only
print(l1)
l1.reverse() #age k piche
print(l1) 
l1.append(69) # add at the end
l1.append(420)
print(l1)
l1.insert(2,434) #add 234 at index 2
print(l1)
l1.pop(4) #remove index 4
print(l1)
l1.remove(69)#remove the element
print(l1)
