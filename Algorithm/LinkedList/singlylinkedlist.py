# Node : save data and next node pointer
# node.next is node's pointer
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, data):
        new_node = Node(data)
        print("start add : %d"%data)
        print("new_node : ", new_node)
        # Head init
        if not self.head:
            self.head = new_node
            print("self_head : ", self.head)
        else:
            node = self.head
            print("new_node.head : ", node)
            # looking for node.next = None
            while node.next:
                node = node.next
                print("node : ",node)
            node.next = new_node
            print("node.next = ", node.next)
        self.count += 1
        print("count : ",self.count)
        print("----------------------------------------------")

    def insert(self, data):
        print("need")

    def delete(self, data):
        node = self.head
        if node.data == data:
            self.head = node.next
            del node
        else:
            while node.next:
                next_node = node.next
                if next_node.data == data:
                    node.next = next_node.next
                    del next_node
                else:
                    node = node.next

    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        
    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

# Test Part
test = SinglyLinkedList()
test.add(1)
test.add(2)
test.add(3)
test.add(4)
test.add(5)
