class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, value):
        new_node = Node(value)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node

        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self

        new_node = Node(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node

        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next

        return self

    # remove the first node with the given value
    def remove_from_front(self):
        runner = self.head
        node_to_remove = runner
        value = node_to_remove.value
        self.head = node_to_remove.next
        node_to_remove = None
        return value

    # remove the last node and return its value
    def remove_from_back(self):
        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        last_node = runner.next
        print(f"**** The value of the removed node is {last_node.value} ****")
        runner.next = None

        return self

    # remove the first node wih the given value
    def remove_val(self, val):
        pass

    # insert a node with value val as the n'th node in the list
    def insert_at(self, value, n):
        pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


my_list = SList()  # create a new instance of a list
test_list = (
    my_list.add_to_front("are")
    .add_to_front("Linked lists")
    .add_to_back("fun!")
    .remove_from_back()
)
# my_list.remove_from_back()

my_list.print_values()
