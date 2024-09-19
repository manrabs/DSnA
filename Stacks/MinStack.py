# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
            
    def pop(self) -> None:
        x = self.stack.pop()
        y = self.min_stack.pop()
        print(x, y)
    
    def top(self) -> None:
        print(self.stack[-1])
        return self.stack[-1]
    
    def getMin(self) -> int:
        print(self.min_stack[-1])
        print(self.min_stack)
        return self.min_stack[-1]

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin() # return -3
    minStack.pop()
    minStack.top()   # return 0
    minStack.getMin() # return -2