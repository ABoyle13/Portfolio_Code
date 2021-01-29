class Circular:

    def __init__(self):
        self.front = 0
        self.rear = 0
        self.size = 0
        self.max_size = 5
        self.q = [" ", " ", " ", " ", " "]

    def add(self, bus):
        if self.size == self.max_size:
            print("The queue is full")
        else:
            self.q.pop(self.rear)
            self.q.insert(self.rear, bus)
            self.rear = (self.rear + 1) % self.max_size
            self.size += 1
            print(self.q)
            return self.q

    def remove(self):
        if self.size == 0:
            print("The queue is empty")
        else:
            self.q.pop(self.front)
            self.q.insert(self.front, ' ')
            self.front += 1
            self.size -= 1
            print(self.q)
            return self.q

    def is_full(self):
        if self.size == self.max_size:
            print("The queue is full")
        else:
            print("The queue is not full")

    def is_empty(self):
        if self.size == 0:
            print("The queue is empty")
        else:
            print("The queue is not empty")


q = Circular()
while True:
    print("\n")
    print("Type 'add' to add an bus to the queue")
    print("Type 'remove' to remove a bus from the queue")
    print("Type 'full' to see if the queue is full")
    print("Type 'empty' to see if the queue is empty")
    print("Type 'exit' to exit the program")
    choice = input("> ")
    if choice == "add":
        item = input("Enter the code of the bus: ")
        q.add(item)
    elif choice == "remove":
        q.remove()
    elif choice == "full":
        q.is_full()
    elif choice == "empty":
        q.is_empty()
    elif choice == "exit":
        break
    else:
        print("Invalid input - please re-enter")
