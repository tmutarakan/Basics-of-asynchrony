from time import time


def gen_filename():
    while True:
        t = int(time() * 1000)
        yield f'file-{t}.jpeg'

        print(234 * 234)


# g = gen_filename()


def gen1(s: str):
    for i in s:
        yield i


def gen2(n: int):
    for i in range(n):
        yield i


g1 = gen1('oleg')
g2 = gen2(4)


tasks = [g1, g2]


while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        ...
