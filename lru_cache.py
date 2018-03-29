class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.ll = DoublyLinkedList(capacity)

    # @return an integer
    def get(self, key):
        return self.ll.get(key)


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        self.ll.put(key, value)

class Node:

    def __init__(self, key, data):
        self.data = data
        self.prev = None
        self.next = None
        self.key = key


class DoublyLinkedList:
    hashmap = {}

    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.length = 0

    def print_list(self):
        temp = self.head
        while(temp is not None):
            temp = temp.next

    def get(self, key):
        if (key not in DoublyLinkedList.hashmap.keys()):
            return -1
        node = DoublyLinkedList.hashmap[key]
        self.delete_node(key)
        self.add_to_top(key, node)
        return node.data

    def put(self, key, data):
        node = DoublyLinkedList.hashmap.get(key)
        if (node is not None):
            node.data = data
            if (self.head != node):
                self.delete_node(key)
                self.add_to_top(key, node)
        else:
            node = Node(key, data)
            if (self.length == self.capacity):
                self.delete_node(self.tail.key)
                self.length -= 1
            self.add_to_top(key, node)
            self.length += 1

    def add_to_top(self, key, node):
        head = self.head
        if (head is None):
            self.head = node
            self.tail = node
        else:
            head.prev = node
            node.next = head
            self.head = node
        DoublyLinkedList.hashmap[key] = node

    def delete_node(self, key):
        node = DoublyLinkedList.hashmap.get(key)
        if (node is None):
            return
        if (node.prev is not None):
            node.prev.next = node.next
        else:
            self.head = node.next
        if (node.next is not None):
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        DoublyLinkedList.hashmap.pop(key)



if __name__ == '__main__':
    ll = DoublyLinkedList(1)
    ll.put(2, 1)
    print(ll.get(2))
    ll.put(3, 2)
    print(ll.get(2))
    print(ll.get(3))

    ll2 = DoublyLinkedList(2)
    ll2.put(2, 1)
    ll2.put(1, 1)
    ll2.put(2, 3)
    ll2.put(4, 1)
    print(ll2.get(1))
    print(ll2.get(2))
