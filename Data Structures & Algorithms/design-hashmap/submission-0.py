class MyHashMap:
    class Node:
        def __init__(self, key: int, val: int):
            self.val = val
            self.key = key
            self.next = None

    def __init__(self):
        self.head = None
        
    def put(self, key: int, value: int) -> None:
        if self.head == None: # Empty LL
            self.head = self.Node(key, value)
            return None

        curr = self.head
        while curr:
            if curr.key == key: # Update Val
                curr.val = value
                return None
            if curr.next == None:
                break
            curr = curr.next
            
        curr.next = self.Node(key, value)

                



    def get(self, key: int) -> int:
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1
        

    def remove(self, key: int) -> None:
        curr = self.head
        prev = None

        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)