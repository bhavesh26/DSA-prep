class Solution:

    def isPossible(self , divisor ,nums):
        ans=0
        for j in range(len(nums)):
                ans+=math.ceil(nums[j]/divisor)
        return ans
        
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        start =1
        end = max(nums)
        while(start<=end):
            mid  = (start+end)//2
            if(self.isPossible(mid , nums) <= threshold):
            
                end = mid-1
            else:
                
                start = mid+1
        return start
           
       
            

        