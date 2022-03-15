#function

def precent(marks): #syntax dekh le bs
    p=sum(marks)/4
    return p

def sum(a,b=0,c=5,d=3): #default parameters idhr bhi hai
    return a+b+c+d

def fact(n):
    if n==0:
        return 1;   
    return n*fact(n-1)
    
n=int(input("Enter n for n!: "))    
print(fact(n))
marks1=[34,54,65,23]
print(precent(marks1))