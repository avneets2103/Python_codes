#q1
n=int(input("Enter the number to print table: "))
for i in range(0,11):
    print(n,"X",i,"=",n*i)
    i=i+1

#q2
l1=["harry","satan","sachin","rahul"]
for i in range(4):
    if l1[i][0]=="s":
        print("Grettings to",l1[i])
    i=i+1

#q3
# easy af

#q4
a=0
n=int(input("Enter the number to check prime: "))
for i in range(2,int((n/2)+1)):
    if n%i==0:
        a=a+1
if a>0:
    print("Non prime")
else:
    print("Prime")

#q5
#easy af

#q6 (factorial)
fact=1
n=int(input("Enter n to find n!: "))
for i in range(1,n+1):
    fact=fact*i
    i=i+1
print(fact)

#q7 star pattern 
#  *  
# ***    
#*****
i=1
j=1
for i in range(1,6):
    for j in range(2):
        print(" ")
        j=j-1
    print("*")
    i=i+2
    
    
        
       
    