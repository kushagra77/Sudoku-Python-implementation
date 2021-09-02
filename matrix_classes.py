class Point():
    def __init__(self, value=0):
        if not given:   
            self.values = {1,2,3,4,5,6,7,8,9}
        self.fixed = (value != 0)
        self.value = value

    def pop(self, value):
        if not self.fixed:
            self.values.discard(value)
            if len(self.values) == 1:
                self.value = self.values.pop()
                self.fixed = True

class Grid():
    def __init__(self):
        self.map = [[{} for i in range(3)] for j in range(3)]
        self.values = []

    def add(self, point, position):
        outer = int(position / 3)
        inner = position % 3
        self.map[outer][inner] = point
        if point.fixed:
            self.values.append(point.value)

    def contains(self, value):
        return value in self.values
            
