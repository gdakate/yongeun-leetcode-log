class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1

                

         
        