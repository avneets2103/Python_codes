#file_i-o

#files are of two types
#text file: .c,.txt etc.
#binary file: .jpg,.dat etc.

#if you dont specify any mode then by defaault it opens in read

from ast import With


f=open('sample.txt','r') #step1 to open in a mode
data=f.read(6) #operators use for your mode and work
print(data) #if character count is specified then it reads only specific data 
f.close() #close the file too 

f=open('sample.txt','r') #step1 to open in a mode
data=f.read() #operators use for your mode and work
print(data) #by deafult it read the full data
f.close() #close the file too 

f=open('sample.txt','r') #step1 to open in a mode
data=f.readline() #read first line only
print(data) 
data=f.readline() #read second line
print(data)
f.close() #close the file too 

f=open("another.txt",'w') #if the file dont exsists it will make its own new file here
f.write("Please write this to the file") #operator for writing in a file
f.close() #dont forget closing the file

f=open("another.txt",'a') #if the file dont exsists it will make its own new file here also it will append or add at the end the new data without erasing the older data
f.write(" write this to the file again.") #operator for writing in a file is same as append if mode is changed
f.close() #dont forget closing the file 

#with statement
#The best way to open and close the file automatically is the with statement

with open("another.txt","r") as f: #as you dont need to close rn
    a=f.read()
with open("sample.txt","a") as f:
    f.write("\nHEY BRO")
print(a)