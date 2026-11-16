def countdown_generator(n: int):
    while n >= 0:
        yield n
        n -= 1


for n in countdown_generator(3):
    print(n)
