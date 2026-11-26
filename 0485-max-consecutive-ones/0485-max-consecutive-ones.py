class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxcount=0
        currentcount =0
        for num in nums:
            if num ==1:
                currentcount+=1
                if currentcount>maxcount:
                    maxcount=currentcount
            else :
                currentcount=0
        return maxcount