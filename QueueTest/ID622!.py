class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k  # total capacity of the queue
        self.len = 0  # currnent capacity of the queue
        self.front = 0  # front pointer/index of the queue
        self.rear = -1  # rear pointer/index of the queue
        self.queue = [None] * k  # QueueTest intialized with given capacity
        return

    def enQueue(self, value: int) -> bool:
        if self.len < self.k:
            # Increment Rear w.r.t k
            self.rear = (self.rear + 1) % self.k
            # Assign the value
            self.queue[self.rear] = value
            # Increment length
            self.len += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.len > 0:
            # Increment Front w.r.t k
            self.front = (self.front + 1) % self.k
            # Decrement length
            self.len -= 1
            return True
        return False

    # If empty return -1 else return the value at front
    def Front(self) -> int:
        return self.queue[self.front] if not self.isEmpty() else -1

    # if empty return -1 else return the value at rear
    def Rear(self) -> int:
        return self.queue[self.rear] if not self.isEmpty() else -1

    # check if queue is empty
    def isEmpty(self) -> bool:
        return False if self.len else True

    # Check if the queue is full
    def isFull(self) -> bool:
        return (self.len == self.k)

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()