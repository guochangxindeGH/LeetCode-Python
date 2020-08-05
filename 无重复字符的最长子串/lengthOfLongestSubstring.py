def lengthOfLongestSubstring(self, s: str):
    occ = set()
    n = len(s)
    rk, ans = -1, 0
    for i in range(n):
        if i != 0:
            occ.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in occ:
            occ.add(s[rk + 1])
            rk += 1
        ans = max(ans, rk + 1 - i)
    return ans


print(lengthOfLongestSubstring("abcabcbb", "abcabcbb"))
