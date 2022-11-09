class PowTwo:
    def __init__(self, Max = 0):
        self.max = Max
        self.n = 0
    def __iter__(self):
        return self
    def __next__(self):
        if (self.n < self.max):
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

x = PowTwo(10)
for i in x:
    print(i, end = ' ')
