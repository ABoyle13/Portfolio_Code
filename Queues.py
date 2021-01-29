queue = [" ", " ", " ", " ", " "]
front = 0
rear = -1
size = 0
maxSize = 5

def enQueue(queue, newItem, rear, size, maxSize):
    if size == maxSize:
        print("Queue full")
    else:
        rear = (rear + 1) % maxSize
        queue[rear] = newItem
        size += 1
    print(queue)
    return queue, rear, size

def deQueue(queue, front, size):
    queue.remove(queue[front])
    queue.insert(front, None)
    front += 1
    size -= 1
    print(queue)
    return queue, front, size

def isEmpty(size):
    if size == 0:
        return True
    else:
        return False

def isFull(size, maxSize):
    if size == maxSize:
        return True
    else:
        return False

while True:
    print("\n")
    print("To add an item, type 'add'")
    print("To remove an item, type 'remove'")
    print("To check if the queue is full, type 'full'")
    print("To check if the queue is empty, type 'empty'")
    answer = input("> ").lower()
    if answer == "add":
        item = input("Enter the item you want to add to the queue: ")
        enQueue(queue, item, rear, size, maxSize)
    elif answer == "remove":
        deQueue(queue, front, size)
    elif answer == "full":
        full = isFull(size, maxSize)
        print(full)
    elif answer == "empty":
        empty = isEmpty(size)
        print(empty)
    else:
        print("Invalid input")
