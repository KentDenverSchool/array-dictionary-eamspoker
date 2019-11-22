import ArrayDictionary


if __name__ == "main":
    dictionary = ArrayDictionary.ArrayDictionary()
    results = "_________ArrayDictionary Tests_________"+
                "\n\nTests in format Test. Expected: Actual: passed:true/false\n\n"
    
    #testing init
    results += dictionary.isEmpty() + " isEmpty for empty constructor. Expected: true Actual: " +
        dictionary.isEmpty() + "\n"
    results += dictionary.size() == 0 + " size for empty constructor. Expected: 0 Actual: " +
        dictionary.size() + "\n"

    #put/contains/get test
    dictionary.put("key1", "value1")

    #test if contains added key.
    results += dictionary.contains("key1") + " Contains. Expected true: Actual: " +
        dictionary.contains("key1") + "\n"
        
    #test if doesn't contain not added key
    results += !dictionary.contains("key2") + " Contains (not added key). Expected false: Actual: "
        + dictionary.contains("key2") + "\n"
    results += dictionary.get("key1") == "value1" + " get. Expected: value1 Actual: "
        + dictionary.get("key1") + "\n"
    results += !dictionary.isEmpty() + " isEmpty. Expected: false Actual: " +
        dictionary.isEmpty() + "\n"
    results += dictionary.size() == 1 + "size. Expected: 1 Actual: " +
        dictionary.size() + "\n\n"
    

    dictionary.put("key2", "value2")

    results += !dictionary.contains("key2") +  " contains  added key. Expected : Actual: "
        + dictionary.contains("key2") + "\n"
    results += dictionary.get("key2") == "value2" + " get added value. Expected: value2 Actual: "
        + dictionary.get("key2") + "\n"
    results += !dictionary.isEmpty() + " isEmpty. Expected: false Actual: " +
        dictionary.isEmpty() + "\n"
    results += dictionary.size() == 2 + " size. Expected: 2 Actual: " +
        dictionary.size() + "\n"

    dictionary.put("key2", "value3")

    results += dictionary.contains("key2") + " contains  added key. Expected true: Actual: " +
        dictionary.contains("key2") + "\n"
    results += dictionary.get("key2") == "value3" + " get changed value. Expected: value3 Actual: "
        + dictionary.get("key2") + "\n"
    results += !dictionary.isEmpty() + " isEmpty. Expected: false Actual: " +
        dictionary.isEmpty() + "\n"
    results += dictionary.size() == 2 + " size. Expected: 2 Actual: " +
        dictionary.size() + "\n"
   
    


    #remove/contains/isEmpty test
    dictionary.remove("key1")

    results += !dictionary.contains("key1") + " doesn't contain removed key. Expected false: Actual: "
        + dictionary.contains("key1") + "\n"
    results += dictionary.contains("key2") + " still contains added key. Expected: true Actual: " +
        dictionary.contains("key2") + "\n"
    results += dictionary.get("key2") == "value3" + " get value. Expected: value3 Actual: "
        + dictionary.get("key2") + "\n"
    results += !dictionary.isEmpty() + " isEmpty for empty constructor. Expected: false Actual: " +
        dictionary.isEmpty() + "\n"
    results += dictionary.size() == 1 + " size. Expected: 1 Actual: " +
        dictionary.size() + "\n"

    dictionary.remove("key2")

    results += !dictionary.contains("key2") + " doesn't contain removed key. Expected false: Actual: "
        + dictionary.contains("key2") + "\n"
    results += !dictionary.isEmpty() + " isEmpty for empty constructor. Expected: false Actual: " +
        dictionary.isEmpty() + "\n"
    results += dictionary.size() == 0 + " size. Expected: 0 Actual: " +
        dictionary.size() + "\n"


    #keys/values test
    dictionary.put("key1", "value1")
    dictionary.put("key2", "value2")
    dictionary.put("key3", "value3")

    keys = dictionary.keys()
    test = 
    keys.remove(key1)
    results += dictionary.contains("key1") + " still contains key. Expected: true Actual: " +
        dictionary.contains("key1") + "\n"

    
    
        
    
    

    
    

    
                
            
    
    logName = input("Enter in log name:\n")
    
