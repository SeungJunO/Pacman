class Counter:
    def __init__(self, initValues=0):
        self.count = initValues
    def rese(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count
