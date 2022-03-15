#strings
b="harry"
print(b)
print(type(b))
c='harry beta'
print(c)
print(type(c))

#concatenation
d=b+c
print(d) 
print(3*b) #3 times write b

#slicing
name="avneet"
n=int(input("Enter a number : "))
print(name[n]) #single element
start=int(input("Enter starting index: ")) #start from start index
end=int(input("Enter the end index: ")) #we reach one less that the number given as end i.e. end-1 index
print(name[start:end]) #start to end  #Output is: vnee [index: 1 to 4]
print(name[start:])#print till the end or already taken as start:6
print(name[:end])#print from starting to a selected end and taken as 0:end
#skip value
skip=int(input("Enter skip value: "))
print(name[start:end:skip])

#string_functions
story='''Once upon a time
there was a coder named 
avneet'''

print(len(story))#tells the length of the string
print(story.endswith("avneet"))
print(story.endswith("ajdsb"))
print(story.count("was"))
print(story.count("a"))
print(story.capitalize())
print(story.find("time")) #first occurance index returned
print(story.replace("avneet","gargie"))

#string_escape_seq.
yo="avneet loves her alot\nbut \'she never\\ heard to\tit\'"
#\' for basic ' in a string and also \\ for normal \ in a string
print(yo)