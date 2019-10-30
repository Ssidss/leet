"""
1005. Maximize Sum Of Array After K Negations
Easy
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.
"""
from heapq import heapify, heappop, heappush
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapify(A)
        for _ in range(K):
            heappush(A, -heappop(A))
        return sum(A)

