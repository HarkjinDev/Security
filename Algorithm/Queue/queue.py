class ListQueue:
    def __init__(self):
        self.my_list = list()
    
    def put(self, element):
        self.my_list.append(element)
    
    def get(self):
        return self.my_list.pop(0)

    def qsize(self):
        return len(self.my_list)

# Test Part
test = ListQueue()
test.put("0")
test.put("1")
test.put("2")

for i in range(0,int(test.qsize())):
    print(test.get())
