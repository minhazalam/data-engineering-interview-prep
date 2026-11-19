class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def search_linked_list(head: Node, target: int) -> bool:
    current = head
    while current is not None:
        if current.data == target:
            return True
        current = current.next
    return False


def insert_at_head(head: Node, value: int) -> Node:
    new_node = Node(value)
    new_node.next = head
    head = new_node
    return head


def insert_at_tail(head: Node, value: int) -> Node:
    new_node = Node(value)
    if head is None:
        head = new_node
        return head
    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = new_node
    tail = new_node
    return head


def delete_at_head(head: Node) -> Node:
    if head is None:
        return None

    head = head.next
    return head


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
current = head

head = insert_at_tail(head, 50)
while current is not None:
    print(current.data)
    current = current.next

# print(search_linked_list(head, 40))
