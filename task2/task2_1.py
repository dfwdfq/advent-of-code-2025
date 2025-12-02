#!/usr/bin/env python3

#taken from https://www.geeksforgeeks.org/dsa/longest-repeating-and-non-overlapping-substring/
def findSuffix(i, j, s, memo):

    # base case
    if j == len(s):
        return 0

    # return memoized value
    if memo[i][j] != -1:
        return memo[i][j]

    # if characters match
    if s[i] == s[j]:
        memo[i][j] = 1 + min(findSuffix(i + 1, j + 1, s, memo), \
                             j - i - 1)
    else:
        memo[i][j] = 0

    return memo[i][j]


def longestSubstring(s):
    n = len(s)

    memo = [[-1] * n for _ in range(n)]

    # find length of non-overlapping
    # substrings for all pairs (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            findSuffix(i, j, s, memo)

    ans = ""
    ansLen = 0

    # If length of suffix is greater
    # than ansLen, update ans and ansLen
    for i in range(n):
        for j in range(i + 1, n):
            if memo[i][j] > ansLen:
                ansLen = memo[i][j]
                ans = s[i:i + ansLen]

    if ansLen > 0:
        return ans

    return "-1"

def is_invalid(s):
    sub = longestSubstring(s)
    rep_count = s.count(sub)
        
    return len(sub)*rep_count == len(s) and not s.startswith("0") and rep_count >= 2

with open("input_test","r") as f:
    data = f.read().strip().split(",")

invalids =[]
for r in data:
    a,b = r.split("-")
    for v in range(int(a),int(b)+1):
        if is_invalid(str(v)):
            invalids.append(v)

print(sum(invalids))
