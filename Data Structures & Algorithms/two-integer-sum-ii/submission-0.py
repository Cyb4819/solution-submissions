class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {} 
        for i, num in enumerate(numbers):
            value = target - num
            if value in seen:
                return [seen[value]+1, i+1]
            seen[num]=i