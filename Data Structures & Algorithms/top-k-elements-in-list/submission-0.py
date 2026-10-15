class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        checkers = {}
        for num in nums:
            checkers[num] = checkers.get(num, 0) + 1
        result = sorted(checkers, key=checkers.get, reverse=True)[:k]
        return result



        