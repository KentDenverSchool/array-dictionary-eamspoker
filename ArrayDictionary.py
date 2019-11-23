import copy
class ArrayDictionary:
    
    def __init__(self):
        self.keys = []
        self.values = []
    
    #add an key-value pair to the dictionary
    def put(self, key, value):
        if key in self.keys:
            self.values[self.keys.index(key)] = value
        else:
            self.keys.append(key)
            self.values.append(value)
        
    #get the value associated with a given key
    def get(self, key):
        return self.values[self.keys.index(key)]

    #remove a key-value pair and return its value
    def remove(self, key):
        if self.contains(key):
            value = self.values[self.keys.index(key)]
            self.values.remove(value)
            self.keys.remove(key)
            return value
        else:
            return null

    #returns true if the given key has an associated value
    def contains(self, key):
        return key in self.keys
          

    #returns true if the dictionary is empty
    def isEmpty(self):
       return not self.keys and not self.values
    

    #returns the number of key-value pairs in the dictionary
    def size(self):
        return len(self.keys)

    #returns a list of keys
    def listKeys(self):
        return copy.deepcopy(self.keys)

    #returns a list of values
    def listValues(self):
        return copy.deepcopy(self.values)


        
