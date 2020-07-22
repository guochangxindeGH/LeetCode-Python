class Solution(object):
    nums = [2, 7, 11, 15]
    target = 9

    def twoSum(self, nums, target):
        lens = len(nums)
        for i in range(1, lens):
            temp = nums[:i]
            breakpoint()
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j > 0:
            return [j, i]

    twoSum(nums, nums, target)
