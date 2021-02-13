class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        self.nums.sort()
        print(self.nums)
        

    def add(self, val)
        self.nums.append(val)
        self.nums.sort()
        return self.nums[::-1][self.k-1]
