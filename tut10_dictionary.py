#dictionery
myDict = {
    "fast":"Quick manner",
    "avneet":"NSUT",
    "marks":[1,2,5],
    "anotherdict":{ #listed dictionery
        "harry":"coder",
        "gargie":"taken"
    },
    1:"haha",
    23:54
}

#using members of dictionery using key values
print(myDict['fast'])
print(myDict['avneet'])
print(myDict["marks"])
print(myDict["anotherdict"]) #accesing full dictionery from a dictionery
print(myDict['anotherdict']['harry']) #accessing members of the listed dict.
print(myDict['anotherdict']['gargie']) 
print(myDict[1])
print(myDict[23])

#dict_methods
print(list(myDict.keys())) #prints the keys of the dict
print(myDict.values()) #prints the keys of the dict.
print(myDict.items()) #prints the (key,value) for all contents of the dictionary
print(myDict)
updateDict={
    "lovish":"friend",
    "divya":"friend",
    "avneet":"broken" #already present key word will get a new value
}
myDict.update(updateDict) #update the dictioneru by adding the key_value pairs from update dict
print(myDict)
print(myDict.get("avneet")) #if key wasent even there it will return none but nt throw error
print(myDict["avneet"]) #if key wwasent there it will return error
