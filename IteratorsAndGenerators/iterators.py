def custom_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("No more to iterate")
            break


custom_for("Hello")
custom_for([1, 2, 3])


class Counter:
    def __init__(self, min, max) -> None:
        self.min = min
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.min < self.max:
            current = self.min
            self.min += 1
            return current
        raise StopIteration


for x in Counter(1, 5):
    print(x)
