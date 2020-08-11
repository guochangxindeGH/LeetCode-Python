class Solution(object):
    # def findMedianSortedArrays(self, nums1, nums2):
    #     p1 = p2 = 0
    #     ls1 = len(nums1)
    #     ls2 = len(nums2)
    #     all_nums = []
    #     median = 0.0
    #     while p1 < ls1 and p2 < ls2:
    #         if nums1[p1] < nums2[p2]:
    #             all_nums.append(nums1[p1])
    #             p1 += 1
    #         else:
    #             all_nums.append(nums2[p2])
    #             p2 += 1
    #     if p1 < ls1:
    #         while p1 < ls1:
    #             all_nums.append(nums1[p1])
    #             p1 += 1
    #     if p2 < ls2:
    #         while p2 < ls2:
    #             all_nums.append(nums2[p2])
    #             p2 += 1
    #     print(all_nums)
    #     if (ls1 + ls2) % 2 == 1:
    #         median = all_nums[(ls1 + ls2) // 2]
    #     else:
    #         median = (all_nums[(ls1 + ls2) // 2] + all_nums[(ls1 + ls2) // 2 - 1]) / 2 * 1.0
    #     return median

    def findMedianSortedArrays(self, nums1, nums2):
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        l = len(nums1)
        if l % 2 == 1:
            return nums1[l // 2]
        else:
            return (nums1[l // 2] + nums1[l // 2 - 1]) / 2


if __name__ == '__main__':
    s = Solution()
    ans = s.findMedianSortedArrays([1, 2], [3, 4])
    print(ans)
