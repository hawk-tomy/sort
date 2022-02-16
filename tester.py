import time


class Timer:
    def __enter__(self):
        self.start = time.time()
    def __exit__(self, *exc_info):
        print(f'{time.time() - self.start}s')


def prepare(num=1000000):
    import random
    target = list(range(1, num+1))
    answer = target[:]
    random.shuffle(target)
    return answer, target


def tester(func, num=1000000):
    answer, target = prepare(num=num)
    print('start')
    with Timer():
        returned = func(target)
    if returned is not None:
        target = returned
    print('end')
    print(answer == target)


def multi_tester(*funcs, num=1000000):
    answer, target = prepare(num=num)
    print('start funcs')
    for i, func in enumerate(funcs, start=1):
        print(f'start {i}')
        temp_target = target[:]
        with Timer():
            returned = func(temp_target)
        if returned is not None:
            temp_target = returned
        print(f'end {i}')
        print(f'{(answer != target)*"not"} success')
    print('end all funcs')
