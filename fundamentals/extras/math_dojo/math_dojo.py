class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        for item in nums:
            self.result += item
        self.result += num
        return self

    def subtract(self, num, *nums):
        for item in nums:
            self.result -= item
        self.result -= num
        return self


# create an instance:
md = MathDojo()
mdm = MathDojo()
# to test:
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5
# run each of the methods a few more times and check the result!
y = mdm.add(2, 78, 3).add(2, 5, 1).subtract(0).result
print(y)
