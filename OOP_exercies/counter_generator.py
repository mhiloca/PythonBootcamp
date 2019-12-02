class CounterUp:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            num = self.start
            self.start += self.step
            return num
        raise StopIteration


class CounterDown:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            num = self.start
            self.start -= self.step
            return num
        raise StopIteration


n = CounterUp(0, 10)
for i in n:
    print(i)
print('- ' * 15)
m = CounterDown(10, 0)
for l in m:
    print(l)

