#q1
hindiDict={
    "pankha":"fan",
    "aalu":"potato",
    "dukhi":"sad"
}

hindi=input("Enter the hindi word from:\n1.pankha\n2.aalu\n3.dukhi\n")
print(hindiDict[hindi])

#or

print("options are",hindiDict.keys())
a=input("Enter the hindi word:\n")
print(hindiDict.get(a)) #dont gives error here rather than syntax error if uh enter invalid thing

#q2
s=set()
for i in range(8):
    a=input("Enter numbers: ")
    s.add(a)
    i=i+1
print(s)

#q3
a={18,"18"} #yes allowed
print(a)
    
#q4
a={20,20.0,"20"}
print(len(a)) #2
print(a) #{20,"20"} as pthon undertsands that 20 = 20.0

#q5
s={}
for i in range (4):
   print("friend ",i+1)
   a=input("Enter your name: ")
   b=input("Enter favt language: ")
   s.update({a:b}) 
print(s)

#q6
s={8,7,12,"Harry",[2,3,4,5]} #nt allowed
