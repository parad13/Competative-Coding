class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    # INSERT METHODS
    def insert_at_begining(self, data):
        node = Node(data = data, next = self.head) # Creating a new node 
        self.head = node # Update the head to the new node(Only for insert at begining)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at_kth_position(self, data, k):
        if k < 1:
            print("Position should be 1 or greater")
            return

        if k == 1:
            self.insert_at_begining(data)
            return

        if k > self.get_length() + 1:
            print(f"Cannot insert at position {k}, as it is out of bounds.")
            return


        if self.head is None:
            print("Linked list is empty")
            return

        count = 1
        itr = self.head
        dataItr = itr.data

        while count < k-1 and itr:
            itr = itr.next
            count += 1

        node = Node(data, itr.next)
        itr.next = node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    
                
    def print(self):
        if self.head is None:
            return "Linked list is empty"
        
        itr = self.head
        listr = ""
        while itr:
            listr += f"[{itr.data}] --> " if itr.next else f"[{itr.data}]" 
            itr = itr.next

        print(listr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["Mango", 'Banana', "Apple", "Cherry"])
    ll.remove_at(2)
    ll.insert_at_kth_position("Peach", 2) # At kth position
    ll.insert_at_kth_position("Peach", 1) # At start
    ll.insert_at_kth_position("Peach", 5) # At end
    print("Length: ", ll.get_length())
    ll.print()

    
