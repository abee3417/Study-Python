class Fib:
    def __init__(self, a = 0, b = 1, Max = 50):
        self.a = a
        self.b = b
        self.max = Max
    def __iter__(self):
        return self
    def __next__(self):
        add = self.a + self.b
        if (add > self.max):
            raise StopIteration
        self.a = self.b
        self.b = add
        return add
    
for i in Fib(Max = 30):
    print(i, end = " ")
