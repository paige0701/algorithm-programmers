"""
Why use linked lists?

pros:
    Linked list can have its elements to be dynamically allocated.
    Linked list nodes can live anywhere in the memory. Array need sequence of memory to be initiated.

cons:
    Linear look up time in O(n). When looking for a value in a linked list, you have to start from the beginning
    and check one element at a time.

"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head


    # Time complexity is O(1)
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # Time complexity is O(n) -> each time method is called,
    # it will always visit every node in the list but only interact with them once, so n* 1 operations
    def size(self):

        current = self.head
        count = 0

        while current:
            count+=1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        if current is None:
            raise ValueError("Data not in the list")

        return current

    def delete(self, data):

        current = self.head

        previous = None
        found = False

        while current and found is False:
            if current.get_data == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError('Data not in the list')

        if previous is None:
            self.head = current.get_next()
        else :
            previous.set_next(current.get_next())
