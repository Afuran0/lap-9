class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


def is_balanced(expression):
    queue = Queue()
    matching_parentheses = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            queue.enqueue(char)
        elif char in ")}]":
            if queue.is_empty() or queue.dequeue() != matching_parentheses[char]:
                return False
# balnce the () if que is emplty 
    return queue.is_empty()


# Test cases 
test_expressions = [
    "()",         
    "({[()]})",    
    "({[)]})",    
    "((",          
    "{[()]}",      
    "{[(])}",      
    "[({})](]",    
    "({{[[(())]]}})"  
]
#print statment 
print("Balanced Parentheses Test Cases:")
for expr in test_expressions:
    result = "Balanced" if is_balanced(expr) else "Not Balanced"
    print(f"{expr}: {result}")
