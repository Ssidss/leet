"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.
"""
class Solution:
    def jump(self, nums: List[int]) -> int:        
        n = len(nums)
        if n == 1:     #[0]
            return 0
        reach = jumpt = endp = 0        
        for i, nm in enumerate(nums):
            reach = max(reach, nm + i)
            if reach >= n-1:       #if end
                return jumpt + 1
            if endp == i:  
                jumpt += 1
                endp = reach

        return jumpt
