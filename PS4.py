#entering inputs from user into a list

fruits=[]
for i in range(7): #starts from 0 on own and goes to 6 i.e. last-1 #i can give initial value by writing like (start,end+1)
    a=input("Enter fruit name\n")
    fruits.append(a)
    i=i+1
print(fruits)

marks=[]
sum=0
for i in range(1,7): 
    m=float(input("Enter marks\n"))
    marks.append(m)
    sum=sum+m
    i=i+1
print(marks)
marks.sort()
print(marks)
print(sum) 
#or
#print(sum(marks)) is an inbuilt function if uh wanna do summation for all integers only in a list

#counting number of zeroes
a=(7,0,8,0,0,9)
cnt=0
for i in range(0,6):
    if a[i]==0:
        cnt=cnt+1
print(cnt)        
#or
print(a.count(0)) #inbuilt function




