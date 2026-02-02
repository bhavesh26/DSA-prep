"""
Brute Force
TC : 
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = -1
        index=1
        while(k>0):
            if(index  not in arr):
                ans = index
                k-=1
            index+=1
        return ans


"""
Optimal Approach using Binary Search
"""
