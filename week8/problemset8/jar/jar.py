class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return self.size * "🍪"


    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Capacity Exceed")

        if n < 0:
            raise ValueError("cannot deposit negative value")

        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not Enough cookies")

        if n < 0:
            raise ValueError("Cannot withdraw a negative number")

        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity=12):
        if capacity < 0:
            raise ValueError("negative capacity value not allowed")

        self._capacity = capacity


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(2)
    print(jar)
    print(jar.capacity)
    print(jar.size)



if __name__ == "__main__":
    main()
