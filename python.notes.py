#1. Import
#   Keyword used for importing any module in our code
#   Modules: Files with the “. py” extension containing Python code that can be imported inside another Python Program.
#   External modules: Need to be downloaded using pip in terminal
#   Internal modules: Can be directly used with [import <module_name>]
#
#2. Different indentation in python
#   '''<something.something.....>''' This is a multiline string in python
# 
#3. Variables and declaration:
#   Python is good enough to understand your variable type on pwn thus you dont write variable type
#   We use [type(<variable_name>)] to get the type of data we are using. 
# 
#4. Operators:
#   We direcly write and, or and not in terms of symbols.
# 
#5. Input:
#   For taking inputs we use the keyword [input(<string_to_show_before_taking_input>]
#   This takes input in terms of string only
#   For taking inputs in other data types, we have to explicitally convert, either in other step or same line.
#   like: int(intput("Enter age: "))
#
#6. Strings"": [MUTTABLE]
#           1.Concatenate: You can easily concatenate strings with '+' and concatenate same string multiple times using '*'
#   
#           2.Slicing:(counting from 0) 
#             a) Single element:- <string_name>[n] for nth index element
#         
#             b) Part of string: (si=start index,fi=final index)
#                    A.<string_name>[si:fi] :- prints string from element 
#                                              si to fi-1.
#                    B.<string_name>[si:] :- From si index to end.
#                    C.<stirng_name>[:fi] :- From start to index fi-1
#         
#             c) String with skip: (sk:skip_value)
#                    <string_name>[si:fi;sk] :- From si to fi-1 with 
#                          skipping sk element after every element taken
# 
#           3.String_methods:
#             a)len(<string_name>): Tells the length of the string.
#             b)<string_name>.endswith(a): Check if string a is at the end of <string_name> or not.                                     
#             c)<string_name>.count(a): Counts the number of time string a comes in <string_name>                               
#             d)<string_name>.capatalize(): Capatlizes the first letter of string.
#             e)<string_name>.find(a): Returns the first occurance index of the string a.                                  
#             f)<string_name>.replace(a,b): Find the string a and replace it  with string b in the given string.                                
#
#7. Lists[]: An array but can contain different data types [MUTTABLE]
#         1.Creating: <list_name>=[elements_seperated_with_comma]
#
#         2.Slicing: //exactly same as a string//
# 
#         3.List_methods:
#           a)len(<list_name>):Tells the length of the list.
#           b)<list_name>.sort: Dont return sorted list, but sort the og list
#           c)<list_name>.reverse: Dont return reversed list but reverse the og list
#           d)<list_name>.append(<element>): Add <element> at the end of list.
#           e)<list_name>.insert(<index_no.>,<element>): Put <element> at <index_no>
#           f)<list_name>.pop(<index_no>): Removes the element at <index_no> from list 
#           g)<list_name>.remove(<element>): Removes <element> from list.
#           h)<list_name>.count(<element>): Returns the <element> count.
#           i)<list_name>.index(<element>): Returns index of the <element> and error if element isnt in list
#
#8. Tuple(): An array but can contain different data types but [IMMUTABLE]
#          1.Creating: <tuple_name>=(elements_seperated_by_commas)
#          
#          2.Slicing: //Same as list and tuple//
# 
#          3.Tuple_methods:
#            a)len(<tuple_name>): Tells the length of tuple.
#            b)<tuple_name>.count(<element>): Returns the <element> count.
#            c)<tuple_name>.index(<element>): Returns the index of the <element>.
#
#9. Dictionary{}: Pair of key and corresponding values [MUTTABLE]
#              1.Creating: <dict_name> = {<key:value> pairs seperated by commas}
#                eg: 
myDict = {
    "fast":"Quick manner",
    "avneet":"NSUT",
    "marks":[1,2,5],
    "anotherdict":{ 
        "harry":"coder",
        "gargie":"taken"
    },
    1:"haha",
    23:54
}
#              2.Accessing data:  NOTE-There is nothing like index in a dictionary.
#                a)Accessing values using key: print(<dict_name>[key])
#                b)Accessing values from a nested dictionary: <parent_dict_name>[<child_dict_name>][<key value>]
# 
#              3.Dict_Methods
#                a)list(<dict_name>.keys()): Lists all the keys of the dictionary.
#                b)<dict_name>.values(): Lists all the values of the dictionary.
#                c)<dict_name>.items(): Lists all the pairs of key and values. [same as print(<dict_name>)
#                d)<dict_name>.update(<another_dict>): It adds the items from <another_dict> to <dict_name> and if same key present then updates its value to new.
#                eg:
updateDict={
    "lovish":"friend",
    "divya":"friend",
    "avneet":"broken" #already present key word will get a new value
}
myDict.update(updateDict)

#10.Set{}:A list but removes any repetition and sorts once uh enter values [MUTTABLE]
#       1.Creating: <set_name>={elemets seperated by comma}
#          NOTE: While creating a empty set it wont work like <set_name>={}
#                Rather you have to <set_name> = set() to make void set.  
#     
#       2. Slicing: It dont have any fixed indices
# 
#       3. Set_Methods:
#          a)len(<set_name>): Returns length of the set
#          b)<set_name>.add(<element>): Adds element which later gets sorted on own
#            Note: You cant add list as an element anywhere as it is mutable, but uh can add tuple as it is immutable
#          c)<set_name>.remove(<element>): Removes tht specific element from set
#          d)<set_name>.pop(): Removes random element from set and prints it
#          e)<set_name>.clear(): Erase all element from set.
#          f)<set_name>.union(<another_set>):Updates <set_name> with union of <set_name> and <another_set>
#          g)<set_name>.union(<another_set>):Updates <set_name> with intersection of <set_name> and <another_set>
#            eg:
c={1,3,5,7,9,2,2}
d=c
c.union({9,4}) #{1,2,3,4,5,7,9}
d.intersection({9,4}) #{9}

#11.Conditionals:
#   None is also a data type in python
#   'is' is also an operator
#   'in' is also an operator
#eg:
a=[1,2,4,54,657]
if 54 in a:
    print("true")

#12.Loops: We use <range> as a keyword in for loops
i=0
while i<10:
    print("yes")
    i=i+1

for i in range(0,7): #[0,1,2,3,4,5,6]
    print(i)

#13.Functions: [Identical to C except Syntax]
#    a)Syntax: 
#      def <function_name>(parameters):
#          <code to be exectued>
#                    
#    b)Default paramter:
#      You can provide default values to paramters from right to left here too.
#
#14.File_IO:
#    a)Opening: f=open('<file name>','<mode>') //Note: You dont need to create any file pointer here
#    1. 'r' mode or read mode
#      A)f.read(a): Returns the content in the file <f> till index number a-1 and if a isnt mentioned then reads the whole file.
#     
#    2. 'w' mode or write mode [If file dont exsist it creates a new one]
#      A)f.write("<string to write after erasing initial data>")
# 
#    3. 'a' mode or append mode [If file dont exsists then make a new and also adds at the end without deleting initial data]
#      A)f.write("<sting to write at the end of initial data>")
# 
#    b)Line by Line reading:
# Method1: 
f=open('sample.txt','r')
for x in f:
    print(x)
f.close()
# Method2:
f=open('sample.txt','r')
f.readline() #reads first line
f.readline() #reads second line and so on.
#    
#    c)Deleting a file: 
import os
os.remove('<file_name>')
#
#    d)Checking if file exsists?:
if os.path.exsists("<file_name>"):
    print(1)
#   
#15.Lamda functions:
# 
#16.OOPS:
# 
#17.D #
