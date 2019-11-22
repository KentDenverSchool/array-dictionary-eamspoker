import ArrayDictionary


if __name__ == "main":
    dictionary = ArrayDictionary.ArrayDictionary()
    results = "_________ArrayDictionary Tests_________"+
                "\n\nTests in format Expected: Actual: passed:true/false\n\n"
    
    #testing init
    results += dictionary.isEmpty() + "isEmpty for empty constructor. Expected: true Actual: " +
        dictionary.isEmpty()
    results += dictionary.size() + "isEmpty for empty constructor. Expected: true Actual: " +
        dictionary.size()

    #put/contains/get test
    dictionary.put("key1", "value1")

    results += dictionary.contains

    
                
            
    
    logName = input("Enter in log name:\n")
    
