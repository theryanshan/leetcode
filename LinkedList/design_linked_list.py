class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        node = ListNode(val)
        if index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            cur = self.head
            while index > 1:
                cur = cur.next
                index -= 1
            node.next = cur.next
            cur.next = node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
        else:
            cur = self.head
            while index > 1:
                cur = cur.next
                index -= 1
            cur.next = cur.next.next
            if not cur.next:
                self.tail = cur
        self.length -= 1
