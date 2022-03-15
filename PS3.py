#practise_set_3

#1 Greetings
name=input("Enter your name: ")
greeting="Good morning "
print(greeting+name)

#2 Customised letter making
letter_template='''Dear <|name|>,
you are selected!

date: <|date|>'''
name=input("Enter your name: ")
date=input("Enter the date: ")
l1=letter_template.replace("<|name|>",name) #you have to save this in another variable ot it wont make any difference as it justs returnds values which can be stored without affecting parent string
l1=l1.replace("<|date|>",date)
print(l1)

#3 Double space detector
st="This is A DOUBLE SPACE  VALI STRING"
a=st.find("  ")
print(a)