class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int):
            raise ValueError("Capacity must be positive integer.")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * '🍪'


    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Capacity exceeded.")
        self.size += n


    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Not enough cookies.")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size cannot exceed Capacity.")
        self._size = size


def main():
    jar = Jar()
    jar.deposit(10)
    print(jar)
    jar.withdraw(5)
    print(jar)

if __name__ == "__main__":
    main()