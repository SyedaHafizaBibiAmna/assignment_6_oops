class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start  # Initialize current

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

countdown = Countdown(5)

for number in countdown:
    print(number)