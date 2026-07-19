class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            speed = (low + high) // 2
            elapsed = 0
            for pile in piles:
                elapsed += math.ceil(pile / speed)
            if elapsed <= h:
                high = speed
            if elapsed > h:
                low = speed + 1
        return low