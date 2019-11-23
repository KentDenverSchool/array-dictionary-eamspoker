import ArrayDictionary

dictionary = ArrayDictionary.ArrayDictionary()
results = "_________ArrayDictionary Tests_________" + "\n\nTests in format Test. Expected: Actual: passed:true/false\n\n"

#testing init
results += str(dictionary.isEmpty()) + " isEmpty for empty constructor. Expected: true Actual: " + str(dictionary.isEmpty()) + "\n"
results += str(dictionary.size() == 0) + " size for empty constructor. Expected: 0 Actual: " + str(dictionary.size()) + "\n"

#put/contains/get test
dictionary.put("key1", "value1")

#test if contains added key.
results += "\n\nPut 2 key values in the dictionary, change the value of one by putting a new value for the old key\n"
results += str(dictionary.contains("key1")) + " Contains. Expected true: Actual: " + str(dictionary.contains("key1")) + "\n"
    
#test if doesn't contain not added key and contains added key, check that it isn't empty, size
results += str(not dictionary.contains("key2")) + " Contains (not added key). Expected: false Actual: " + str(dictionary.contains("key2")) + "\n"
results += str(dictionary.get("key1") == "value1") + " get. Expected: value1 Actual: " + dictionary.get("key1") + "\n"
results += str(not dictionary.isEmpty()) + " isEmpty. Expected: false Actual: " + str(dictionary.isEmpty()) + "\n"
results += str(dictionary.size() == 1) + " size. Expected: 1 Actual: " + str(dictionary.size()) + "\n"

results += "2nd add:\n"
dictionary.put("key2", "value2")
#test if contains added key, that is isn't empty, size
results += str(dictionary.contains("key2")) +  " contains added key. Expected: false Actual: " + str(dictionary.contains("key2")) + "\n"
results += str(dictionary.get("key2") == "value2") + " get added value. Expected: value2 Actual: " + dictionary.get("key2") + "\n"
results += str(not dictionary.isEmpty()) + " isEmpty. Expected: false Actual: " + str(dictionary.isEmpty()) + "\n"
results += str(dictionary.size() == 2) + " size. Expected: 2 Actual: " + str(dictionary.size()) + "\n"

dictionary.put("key2", "value3")

results += "Change 2nd value:\n"
#test if contains added key, that is isn't empty, size
results += str(dictionary.contains("key2")) + " contains added key. Expected true: Actual: " + str(dictionary.contains("key2")) + "\n"
results += str(dictionary.get("key2") == "value3") + " get changed value. Expected: value3 Actual: " + dictionary.get("key2") + "\n"
results += str(not dictionary.isEmpty()) + " isEmpty. Expected: false Actual: " + str(dictionary.isEmpty()) + "\n"
results += str(dictionary.size() == 2) + " size. Expected: 2 Actual: " + str(dictionary.size()) + "\n\n"




#remove/contains/isEmpty test

results += "\nRemove the 2 values from the dictionary, check isEmpty"
dictionary.remove("key1")

#check if it removed value, still contains not removed value, size, isEmpty
results += str(not dictionary.contains("key1")) + " doesn't contain removed key. Expected false: Actual: " + str(dictionary.contains("key1")) + "\n"
results += str(dictionary.contains("key2")) + " still contains added key. Expected: true Actual: " + str(dictionary.contains("key2")) + "\n"
results += str(dictionary.get("key2") == "value3") + " get value. Expected: value3 Actual: " + str(dictionary.get("key2") + "\n")
results += str(not dictionary.isEmpty()) + " isEmpty for empty constructor. Expected: false Actual: " + str(dictionary.isEmpty()) + "\n"
results += str(dictionary.size() == 1) + " size. Expected: 1 Actual: " + str(dictionary.size()) + "\n"

dictionary.remove("key2")
#checked if it removed the value, size, isEmpty
results += str(not dictionary.contains("key2")) + " doesn't contain removed key. Expected false: Actual: " + str(dictionary.contains("key2")) + "\n"
results += str(dictionary.isEmpty()) + " isEmpty. Expected: true Actual: " + str(dictionary.isEmpty()) + "\n"
results += str(dictionary.size() == 0) + " size. Expected: 0 Actual: " + str(dictionary.size()) + "\n\n"



#keys/values test
dictionary.put("key1", "value1")
dictionary.put("key2", "value2")
dictionary.put("key3", "value3")

#check if editing the copy will affect the instance data
results += "\nGet keys and values list, modify lists and see if the instance data of the dictionary is modified.\n"
keyList = dictionary.listKeys()
keyList.remove("key1")
results += str(dictionary.contains("key1")) + " still contains key. Expected: true Actual: " + str(dictionary.contains("key1")) + "\n"

valuesList = dictionary.listValues()
valuesList.remove("value1")
values2 = dictionary.listValues()
results += str("value1" in values2) + " still contains value. Expected: true Actual: " + str(dictionary.contains("key1")) + "\n"


logName = input("Enter in log name:\n")

with open(logName, 'w') as log:
    log.write(results)
    
