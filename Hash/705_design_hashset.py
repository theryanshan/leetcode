# Time: O(1) in average
# Space: O(n)
# Tip:
# 1. we know the maximum add from question, so define capacity to be 10 ** 4 to skip rehashing
# 2. use a dummy node as head node, and chaining to handle hash collision. e.g. for key 1, 10001, 20001,they all have the same hash value 1, so we chain them together


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.set[key % (10**4)]
        while cur.next:
            if cur.next.val == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % (10**4)]
        while cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % (10**4)]
        while cur.next:
            if cur.next.val == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
