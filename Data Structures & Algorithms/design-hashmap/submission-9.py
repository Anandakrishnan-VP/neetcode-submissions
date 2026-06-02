class MyHashMap:

    def __init__(self):
        self.hashsize=883
        self.hashmap= [[]for i in range(self.hashsize)]
    
    def hashvalue(self,key):
        return key % self.hashsize

    def put(self, key: int, value: int) -> None:
        h=self.hashvalue(key)

        for pair in self.hashmap[h]:
            if pair[0]==key:
                pair[1]=value
                return
        self.hashmap[h].append([key,value])
        

    def get(self, key: int) -> int:
        h=self.hashvalue(key)
        
        for pair in self.hashmap[h]:
            if pair[0]==key:
                return pair[1]
        return -1
        

    def remove(self, key: int) -> None:
        h=self.hashvalue(key)

        for pair in self.hashmap[h]:
            if pair[0]==key:
                self.hashmap[h].remove(pair)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)