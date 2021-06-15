# Stack in python
class ListStack:
    def __init__(self):
        self.my_list = list()

    def push(self, data):
        self.my_list.append(data)
    
    def pop(self):
        return self.my_list.pop()

    def qsize(self):
        return len(self.my_list)

# Test Part
test = ListStack()
test.push("0")
test.push("1")
test.push("2")

for i in range(0,int(test.qsize())):
    print(test.pop())
