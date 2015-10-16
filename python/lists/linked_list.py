#!/usr/bin/python

class LinkedListNode(object):
    # A simple linked list node
    def __init__(self, value=0, nextNode=None):
        self.value = value
        self._next = nextNode
        return

class LinkedList(object):
    def __init__(self):
        self.first = None
        return

    def insert(self, value):
        # O(n)
        newNode = LinkedListNode(value, None)
        if not self.first:
            self.first = newNode
            return

        t = self.first
        while t._next:
            t = t._next

        t._next = newNode
        return

    def insert_after(self, value_prev, value):
        # O(n)
        newNode = LinkedListNode(value, None)
        if not self.first:
            self.first = newNode
            return

        t = self.first
        while t._next:
            if t._next.value > value_prev:
                break
            t = t._next

        newNode._next = t._next
        t._next = newNode
        return

    def delete(self, value):
        # O(n)
        t = self.first
        prev = None
        while t:
            if t.value == value:
                break
            prev = t
            t = t._next
      
        if prev: 
            prev._next = t._next
        else:
            self.first = None
        return

    def delete_at(self, index):
        cnt = 0
        t = self.first
        prev = None
        while t:
            if cnt == index:
                if prev:
                    prev._next = t._next
                else:
                    self.first = None
                break
            prev = t
            t = t._next
            cnt += 1

        return

    def push(self, value):
        # O(1)
        newNode = LinkedListNode(value, self.first)
        self.first = newNode
        return

    def pop(self):
        # O(1)
        if self.first:
            ret = self.first.value
            self.first = self.first._next
            return ret
        else:
            return None

    def swap_at(self, index_first, index_second):
        if index_first == index_second:
            return

        # Ensure that the indices are sorted
        if index_first > index_second:
            index_first = index_second + index_first
            index_second = index_first - index_second
            index_first = index_first - index_second

        f = None
        fprev = None
        s = None
        sprev = None
        t = self.first
        prev = None
        cnt = 0
        while t:
            if cnt == index_first:
                f = t
                fprev = prev

            if cnt == index_second:
                s = t
                sprev = prev
                break

            cnt += 1
            prev = t
            t = t._next

        if not f:
            raise IndexError("First element not found")

        if not s:
            raise IndexError("Second element not found")

        # We'll need this soon
        secondnext = s._next

        if f._next == s:
            s._next = f
        else:
            s._next = f._next

        if fprev:
            fprev._next = s

        if f==self.first:
            self.first = s

        f._next = secondnext

        if sprev and sprev != f:
            sprev._next = f
        return

    def kth(self, k):
        cnt = 0
        t = self.first
        while t:
            if cnt == k:
                return t.value
                break
            cnt += 1
            t = t._next

        return None

    def last_kth(self, k):
        cnt = 0
        t = self.first
        ref = None
        while t:
            if cnt == k:
                break

            cnt = cnt + 1
            t = t._next

        ret = self.first
        while t:
            ret = ret._next
            t = t._next

        return ret.value

    def count(self, value):
        # O(n)
        t = self.first
        count = 0
        while t:
            if t.value == value:
                count += 1
            t = t._next

        return count

    def reverse(self):
        t = self.first
        prev = None
        while t:
            nxt = t._next
            if nxt == None:
                self.first = t
            t._next = prev
            prev = t
            t = nxt

        return

    def __len__(self):
        # O(n)
        length = 0
        t = self.first
        while t:
            length += 1
            t = t._next

        return length

    def __contains__(self, value):
        # O(n)
        t = self.first
        while t:
            if t.value == value:
                return True

            t = t._next

        return False

    def __str__(self):
        # O(n)
        t = self.first
        is_first = True
        ret = ""
        ret = "["
        while t:
            if not is_first:
                ret += ", "
                is_first = False
            ret += str(t.value)
            t = t._next
        ret += "]"
        return ret

    def toList(self):
        # O(n)
        t = self.first
        ret = []
        while t:
            ret.append(t.value)
            t = t._next
        return ret

if __name__ == '__main__':
    main()
