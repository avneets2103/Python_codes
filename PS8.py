#q4
def sum(n):
    if n==1:
        return 1;
    return n+sum(n-1)

n=int(input("Enter n to find sum of n naturals: "))
print(sum(n))

#q5
def pattern(n):
    for i in range(n):
        print("* "*(n-i))
        
n=int(input("Enter n for star pattern: "))
pattern(n)