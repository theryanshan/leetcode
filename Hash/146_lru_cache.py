# Tip:
# we can use double linked list + hashmap to implement LRU cache
# use head and tail to point at the  most recent use and LRU
# create remove function to remove a node from the list
# create insert function to insert a node to the head of the list


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        prev = next = None


class LRUCache:
    def __init__(self, capacity: int):
        # head = most recent use, tail = LRU
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map.keys():
            return -1
        node = self.map.get(key)
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            node = self.map.get(key)
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.insert(node)
            self.map[key] = node
            if len(self.map) > self.capacity:
                lastNode = self.tail.prev
                del self.map[lastNode.key]
                self.remove(lastNode)

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node):
        prev, next = self.head, self.head.next
        self.head.next = next.prev = node
        node.next, node.prev = next, prev


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # returns 1
    cache.put(3, 3)  # evicts key 2
    print(cache.get(2))  # returns -1 (not found)
    cache.put(4, 4)  # evicts key 1
    print(cache.get(1))  # returns -1 (not found)
    print(cache.get(3))  # returns 3
    print(cache.get(4))  # returns 4
