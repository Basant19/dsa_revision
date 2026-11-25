class Solution:
    from collections import Counter

    def sumOfUnique(self, nums: list[int]) -> int:
        sum = 0
        count = Counter(nums)
        for number, freq in count.items():
            if freq == 1:
                sum += number
        return sum
