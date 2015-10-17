#!/usr/bin/python


class Stack(object):
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def reverse(self):
        def _recursion():
            if self.is_empty():
                return

            val = self.pop()
            _recursion()
            self._insert_at_bottom(val)
            return 

        _recursion()
            
        return

    def _insert_at_bottom(self, value):
        self._items.insert(0, value)

def infix_to_postfix(expr):
    s = Stack()
    
    def _priority(operator):
        # Helper method to return the priority of operators
        if operator == '+' or operator == '-':
            return 0
        elif operator == '*' or operator == '/':
            return 1
        elif operator == '^':
            return 2

    def _is_operator(char):
        # Helper method to check if a character is an operator or an operaand
        if char in "+ - ^ * / ( )".split():
            return True

        return False

    ret = ""
    for ch in expr:
        isop = _is_operator(ch)

        if not isop:
            ret += ch
            continue

        priority = _priority(ch)
        if ch == ')':
            while not s.is_empty():
                char = s.pop()
                if char == '(':
                    break
                ret += char

        elif ch == '(':
            s.push(ch)
        else:
            while not s.is_empty() and _priority(s.peek()) >= priority:
                char = s.pop()
                if char != '(' and char != ')':
                    ret += char

            s.push(ch)

    while not s.is_empty():
        char = s.pop()
        ret += char

    return ret

def evaluatePostfix(expr):
    def _is_operator(char):
        # Helper method to check if a character is an operator or an operaand
        if char in "+ - ^ * / ( )".split():
            return True

        return False

    s = Stack()
    for ch in expr:
        isop = _is_operator(ch)
        if not isop:
            s.push(ch)
            continue

        op2 = float(s.pop())
        op1 = float(s.pop())

        if ch == '+':
            s.push(op1 + op2)
        elif ch=='-':
            s.push(op1 - op2)
        elif ch=='/':
            s.push(op1 / op2)
        elif ch=='*':
            s.push(op1 * op2)

    return float(s.pop())

def main():
    exprs = ["a+b*c", "a+b*c-d/e", 'a*(b+c)']
    answer = ['abc*+', 'abc*+de/-', 'abc+*']
    for expr, ans in zip(exprs, answer):
        out = infix_to_postfix(expr)
        assert(out == ans)

    exprs = ['58+9-', '123*+45/-']
    answer = [4, 6.2]
    for expr, ans in zip(exprs, answer):
        out = evaluatePostfix(expr)
        assert(ans == out)

if __name__ == '__main__':
    main()
