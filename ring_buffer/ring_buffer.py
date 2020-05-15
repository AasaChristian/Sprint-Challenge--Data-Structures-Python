from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.order = {}
        self.size = 0

    # def append(self, item):
    #     if self.size == self.capacity:
    #         self.storage.remove_from_head()
    #         self.size -=1
    #     self.storage.add_to_tail(item)
    #     self.size +=1
    def append(self, item):
        if self.size == self.capacity:
            self.storage.remove_from_head()
        self.storage.add_to_tail((self.size, item))
        self.order[self.size]
        self.size +=1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        list_buffer_contents.append(self.storage.head.value)
        while self.storage.head.next:
            list_buffer_contents.append(self.storage.head.value)
            print(self.storage.head.values)

        
        return list_buffer_contents


lister = RingBuffer(3)
lister.append("a")
lister.append("b")
lister.append("c")
lister.get()
# TODO: Your code here
# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
