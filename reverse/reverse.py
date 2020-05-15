class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        # if not node:
        #     return None
        # head = node 
        # if node.next_node:
        #     new_head = node.next_node
        # future_head = None
        # node.next_node = None
        # while new_head is not None:
        #     future_head = new_head.next_node
        #     new_head.next_node = head
        #     head = new_head
        #     new_head = future_head
        # return head
        
        head = node
        if not node:
            return None
        if self.head.next_node:
            print(head.value)
            return self.reverse_list(head.next_node, head)
        else:
            return node
    
