class Solution(object):
    def reverseString(self, s):
        reverse = s + []
        for i in range(len(reverse)):
            s[len(reverse) - i - 1] = reverse[i]
