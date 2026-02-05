"""
similar to book allocation problem
i faced challenge in this problem
Memorize the binary search rule: if searching for a minimum valid answer, 
move left when valid; if searching for a maximum,
 move right when valid.


"""
class Solution:
    def isPossible(self,nums, k , i):
        count = 1
        rs = 0
        for s in nums:
            if s + rs <=i:
                rs+=s
            else:
                count+=1
                rs=s

        return count

    def splitArray(self, nums: List[int], k: int) -> int:
        start = max(nums)
        end = sum(nums)
        while(start<=end):
            mid = (start+end)//2
            ans = self.isPossible(nums, k  , mid)
            if(ans <= k):
                end = mid-1
            else:
                start = mid+1
        return start
        # for i in range(start , end+1):
        #     if self.isPossible(nums  , k , i)==k:
        #         return i
        # return start
        
        