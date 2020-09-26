class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        if len(self.storage) == 0:
            self.storage.append(item)
        else:
            if len(self.storage) == self.capacity:
                if self.index == self.capacity:
                    self.index -= self.capacity
                    self.storage[self.index] = item
                    self.index += 1
                else:
                    self.storage[self.index] = item
                    self.index += 1
            else:
                self.storage.append(item)

    def get(self):
        return self.storage
