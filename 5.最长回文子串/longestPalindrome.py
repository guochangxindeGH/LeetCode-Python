class Solution:
    # 笨蛋算法是不行滴
    # def longestPalindrome(self, s: str) -> str:
    #     # 特判
    #     size = len(s)
    #     if size < 2:
    #         return s
    #
    #     max_len = 1
    #     res = s[0]
    #
    #     # 枚举所有长度大于等于 2 的子串
    #     for i in range(size - 1):
    #         for j in range(i + 1, size):
    #             if j - i + 1 > max_len and self.__valid(s, i, j):
    #                 max_len = j - i + 1
    #                 res = s[i:j + 1]
    #     return res
    #
    # def __valid(self, s, left, right):
    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         else:
    #             left += 1
    #             right -= 1
    #     return True

    # 动态规划法
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     if n < 2:
    #         return s
    #     dp = [[False] * n for _ in range(n)]
    #     ans = s[0]
    #     for i in range(n):
    #         dp[i][i] = True
    #     for j in range(1, n):
    #         for i in range(0, j):
    #             if s[i] == s[j]:
    #                 if j - i < 3:
    #                     dp[i][j] = True
    #                 else:
    #                     dp[i][j] = dp[i + 1][j - 1]
    #             else:
    #                 dp[i][j] = False
    #             if dp[i][j]:
    #                 if j - i + 1 > len(ans):
    #                     ans = s[i: j + 1]
    #     return ans

    # 中心扩散法
    # def longestPalindrome(self, s: str) -> str:
    #     size = len(s)
    #     if size < 2:
    #         return s
    #     max_len = 1
    #     res = s[0]
    #     for i in range(size):
    #         palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
    #         palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)
    #         cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
    #         if len(cur_max_sub) > max_len:
    #             max_len = len(cur_max_sub)
    #             res = cur_max_sub
    #     return res
    #
    #
    # def __center_spread(self, s, size, left, right):
    #     """
    #     left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
    #     right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
    #     """
    #     i = left
    #     j = right
    #     while i >= 0 and j < size and s[i] == s[j]:
    #         i -= 1
    #         j += 1
    #     return s[i + 1 : j], j - i - 1

    # 更快的方法
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s
        max_len, start = 1, 0
        for i in range(1, n):
            even = s[i - max_len: i + 1]
            odd = s[i - max_len - 1: i + 1]
            if i - max_len - 1 >= 0 and odd == odd[:: -1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[:: -1]:
                start = i - max_len
                max_len += 1
        return s[start: start + max_len]

s = Solution()
lll = 'abade'
print(s.longestPalindrome(lll))
