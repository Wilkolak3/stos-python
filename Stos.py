class Stos:
    def __init__(self):
        self.elementy = []

    def push(self, rzeczy):
        self.elementy.append(rzeczy)

    def pop(self):
        if self.is_empty():
            return 0
        return self.elementy.pop()

    def top(self):
        if self.is_empty():
            return 0
        return self.elementy[-1]

    def is_empty(self):
        return len(self.elementy) == 0

