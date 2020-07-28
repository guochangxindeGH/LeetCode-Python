class Solution(object):
    nums = [2, 7, 11, 15]
    target = 9

    def twoSum(self, nums, target):
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            temp = nums[:i]
            # breakpoint()
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j >= 0:
            return [j, i]

    def twoSum2(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if (hashmap.get(target - num) is not None):
                return [hashmap.get(target - num), i]
            hashmap[num] = i

    def twoSum3(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]

    print(twoSum2(nums, nums, target))
