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

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        ans = s[0]

        for i in range(n):
            dp[i][i] = True

        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    if j - i + 1 > len(ans):
                        ans = s[i: j + 1]
        return ans



s = Solution()
lll = 'aaaa'
print(s.longestPalindrome(lll))
