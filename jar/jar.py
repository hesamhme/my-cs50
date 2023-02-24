class Jar:
    def __init__(self, zarfiat=12, size=0):
        if zarfiat < 0 or int(zarfiat) != zarfiat:
            raise ValueError
        else:
            self._zarfiat = zarfiat

        if size < 0 or int(size) != size:
            raise ValueError
        else:
            self._size = size

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        self._size += n
        if self._size > self.zarfiat:
            raise ValueError

    def withdraw(self, n):
        self._size -= n
        if self._size < 0:
            raise ValueError

    @property
    def zarfiat(self):
        return self._zarfiat

    @property
    def size(self):
        return self._size
