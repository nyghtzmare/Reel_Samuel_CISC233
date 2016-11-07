class chain_hash_key:
    def __init__(self, size):
        self.size = size
        self.slots = [[None]] * self.size
        self.data = [[None]] * self.size

    def __getitem__(self, item):
        index = self.hashfunction(item, self.size)
        inner = self.slots[index]
        answer = self.data[index]
        if len(inner) > 1:
            for x in range(0, len(inner)):
                if inner[x] == item:
                    return answer[x]

        else:
            if inner[0] == item:
                return answer[0]


    def put(self, key, data):
        hash_value = self.hashfunction(key, len(self.slots))

        if self.slots[hash_value] == [None]:
            self.slots[hash_value] = [key]
            self.data[hash_value] = [data]

        elif self.slots[hash_value] == [key]:
            self.data[hash_value] = [data]

        else:
            self.slots[hash_value].append(key)
            self.data[hash_value].append(data)

    def hashfunction(self, key, size):
        return key % size

call = chain_hash_key(10)

call.put(10, "cat")
call.put(100, "dog")
call.put(87, "bunny")
call.put(30, "pig")
call.put(49, "elephant")
print call.data
print call.slots
print call[30]