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
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l + 1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j == len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i: j + 1]
        return ans


s = Solution()
lll = 'abcda'
print(s.longestPalindrome(lll))
