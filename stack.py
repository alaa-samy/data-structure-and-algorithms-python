# Stack implementation in python

# Create stack
def create_stack():
    stack = []
    return stack
    
#Check if the stack is empty 
def check_empty(stack):
    return len(stack) == 0
    
# Add items to the stack
def push_item(stack , item):
    stack.append(item)
    return stack
    
# Remove item from the stack
def pop_item(stack):
    if check_empty(stack):
        return "The stack is empty"
    return stack.pop()
    
stack = create_stack()
push_item(stack , 2)
push_item(stack , 5)
push_item(stack , 9)
print(stack)
pop_item(stack)
print(stack)
