class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, f in freq.items():
            buckets[f].append(num)
        result = []
        for f in range(n, 0, -1):
            for num in buckets[f]:
                result.append(num)
                if len(result) == k:
                    return result