class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result=num+sum(nums)
        return self.result
    def subtract(self, num, *nums):
        self.result = num - sum(nums)
        return self.result
md = MathDojo()
res0 = md.add(2,6,6,6)
print(res0)
res1 = md.subtract(10,2,2,6)
print(res1)

# to test:
# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x)    # should print 5
# run each of the methods a few more times and check the result!