
import pytest

from dsa.linked_list.linked_list_basics import (
    Node,
    delete_at_head,
    insert_at_head,
    insert_at_tail,
    search_linked_list,
)


def build_linked_list(values):
    """Build a linked list from a Python list."""
    head = None
    tail = None

    for value in values:
        new_node = Node(value)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


def linked_list_to_list(head):
    """Convert a linked list into a Python list for assertions."""
    result = []
    current = head

    while current is not None:
        result.append(current.data)
        current = current.next

    return result


# -------------------------
# Search Linked List Tests
# -------------------------

@pytest.mark.parametrize(
    "values, target, expected",
    [
        ([10, 20, 30, 40], 30, True),
        ([10, 20, 30, 40], 10, True),
        ([10, 20, 30, 40], 40, True),
        ([10, 20, 30, 40], 50, False),
        ([], 10, False),
        ([10], 10, True),
    ],
)
def test_search_linked_list(values, target, expected):
    head = build_linked_list(values)

    assert search_linked_list(head, target) is expected


# -------------------------
# Insert At Head Tests
# -------------------------

def test_insert_at_head_empty_list():
    head = None

    head = insert_at_head(head, 5)

    assert linked_list_to_list(head) == [5]


def test_insert_at_head_non_empty_list():
    head = build_linked_list([10, 20, 30])

    head = insert_at_head(head, 5)

    assert linked_list_to_list(head) == [5, 10, 20, 30]


def test_insert_at_head_multiple_times():
    head = build_linked_list([10, 20, 30])

    head = insert_at_head(head, 5)
    head = insert_at_head(head, 2)

    assert linked_list_to_list(head) == [2, 5, 10, 20, 30]


# -------------------------
# Insert At Tail Tests
# -------------------------

def test_insert_at_tail_empty_list():
    head = None

    head = insert_at_tail(head, 40)

    assert linked_list_to_list(head) == [40]


def test_insert_at_tail_non_empty_list():
    head = build_linked_list([10, 20, 30])

    head = insert_at_tail(head, 40)

    assert linked_list_to_list(head) == [10, 20, 30, 40]


def test_insert_at_tail_single_node():
    head = build_linked_list([10])

    head = insert_at_tail(head, 20)

    assert linked_list_to_list(head) == [10, 20]


def test_insert_at_tail_multiple_times():
    head = build_linked_list([10])

    head = insert_at_tail(head, 20)
    head = insert_at_tail(head, 30)

    assert linked_list_to_list(head) == [10, 20, 30]


# -------------------------
# Delete At Head Tests
# -------------------------

def test_delete_at_head_empty_list():
    head = None

    head = delete_at_head(head)

    assert head is None


def test_delete_at_head_single_node():
    head = build_linked_list([10])

    head = delete_at_head(head)

    assert head is None


def test_delete_at_head_multiple_nodes():
    head = build_linked_list([10, 20, 30])

    head = delete_at_head(head)

    assert linked_list_to_list(head) == [20, 30]


def test_delete_at_head_repeatedly():
    head = build_linked_list([10, 20, 30])

    head = delete_at_head(head)
    head = delete_at_head(head)
    head = delete_at_head(head)

    assert head is None
