#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1
