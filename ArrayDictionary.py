import copy
class ArrayDictionary:
    
    def __init__(self):
        self.keys = []
        self.values = []
    
    #adds an key-value pair to the dictionary, takes in a key and a value 
    def put(self, key, value):
        if key in self.keys:
            self.values[self.keys.index(key)] = value
        else:
            self.keys.append(key)
            self.values.append(value)
        
    #get the value associated with a given key, takes in a key
    def get(self, key):
        return self.values[self.keys.index(key)]

    #removes a key-value pair, returns its value, takes in a key
    def remove(self, key):
        if self.contains(key):
            value = self.values[self.keys.index(key)]
            self.values.remove(value)
            self.keys.remove(key)
            return value
        else:
            return null

    #returns true if the given key has an associated value, takes in a key
    def contains(self, key):
        return key in self.keys
          

    #returns true if the dictionary is empty, no parameters
    def isEmpty(self):
       return not self.keys and not self.values
    

    #returns the number of key-value pairs in the dictionary, no parameters
    def size(self):
        return len(self.keys)

    #returns a list of keys, no parameters
    def getKeys(self):
        return copy.deepcopy(self.keys)

    #returns a list of values, no parameters
    def getValues(self):
        return copy.deepcopy(self.values)


        
