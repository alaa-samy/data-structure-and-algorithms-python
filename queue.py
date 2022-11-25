# Queue implementation in python

# Create queue
def create_queue():
    queue = []
    return queue
    
#Check if the queue is empty 
def check_empty(queue):
    return len(queue) == 0
    
# Add items to the queue
def enqueue(queue , item):
    queue.append(item)
    return queue
    
# Remove item from the queue
def dequeue(queue):
    if check_empty(queue):
        return "The queue is empty"
    return queue.pop(0)
    
queue = create_queue()
enqueue(queue , 2)
enqueue(queue , 5)
enqueue(queue , 7)
print(queue)
dequeue(queue)
print(queue)
