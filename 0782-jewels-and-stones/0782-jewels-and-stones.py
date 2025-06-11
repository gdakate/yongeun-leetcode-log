class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sets = set(jewels)
        return sum(i in sets for i in stones)
        