class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)

        dif = t_count-s_count

        return list(dif.keys())[0]