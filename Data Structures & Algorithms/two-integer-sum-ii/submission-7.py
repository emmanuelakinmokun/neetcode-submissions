class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        vault = {}
        for i, num in enumerate(numbers):
            complement = target-num
            if complement in vault:
                return[vault[complement]+1, i+1]
            vault[num] = i
