class Countdown:
    def __init__(self, n):
        self._n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self._n < 0:
            raise StopIteration
        current_val = self._n
        self._n = self._n - 1
        return current_val


countdown = Countdown(3)

print(next(countdown))  # 3
print(next(countdown))  # 2
print(next(countdown))  # 1
print(next(countdown))  # 0
# print(next(countdown))  # StopIteration
