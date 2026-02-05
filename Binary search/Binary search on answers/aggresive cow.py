"""
Intution is simple to check whether we can play the cows at particular distacne or not
"""

class Solution:
    
    def isPossible(self,stalls,k , distance):
        count = 1
        lastPosition = stalls[0]
        for stall in stalls:
            if stall - lastPosition >=distance:
                count+=1
                lastPosition = stall
            if(count>=k):
                return True
        return False
        
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        ans = -1
        end = stalls[-1] - stalls[0]
        start  =1
        while(start <=end):
            mid  = (start+end)//2
            if(self.isPossible(stalls, k , mid)):
                ans = mid
                start  = mid+1
            else:
                end = mid-1
        return ans
        
        # for distance in range(1 , maxDistance+1):
        #     if self.isPossible(stalls , k , distance):
        #         ans = distance
        # return ans
            
        