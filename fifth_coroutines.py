class BlaBlaException(Exception):
    ...


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


def subgen():
    x = 'Ready to accept message'
    message = yield x
    print(f'Subgen received: {message}')


@coroutine
def average():
    count = 0
    summa = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
            break
        except BlaBlaException:
            print('.' * 80)
            break
        else:
            count += 1
            summa += x
            average = round(summa / count, 2)

    return average
