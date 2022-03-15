import os
#q3 Important question

# for i in range(2,21):
#     with open("multiplication_table_of_{i}.txt","w")as f:
#         for j in range(1,11):
#             f.write(f"{i}X{j}={i*j}\n")
#             if j!=10:
#                 f.write('\n')

#q5 bsdk txt file save to kr dia kr

censored=["donkey","motherfucking"]
with open("donkey.txt","r")as f:
    content=f.read()

for i in range(len(censored)):
    content=content.replace(censored[i],"#"*len(censored[i]))
    print(content)
with open("donkey.txt","w")as f:
        f.write(content)

#q6
copied=""
with open("initial.txt","r")as f:
    copied=copied+f.read()
with open("this.txt","w")as f:
    f.write(copied)

#q renamed 
#old file ko copy krle with final name to another file and delete the og file

#deleting a file in os module
#eg: 
os.remove("initial.txt")

