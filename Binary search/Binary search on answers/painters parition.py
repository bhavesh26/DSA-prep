class Solution:
    
    
    def isPossible(self, arr ,  k, time):
        count =1
        t = 0
        for i in arr:
            if i + t <=time:
                t+=i
            else:
                count+=1
                t = i
        return count
        
    
    
    def minTime (self, arr, k):
        start = max(arr)
        end  = sum(arr)
        while(start <=end):
            mid = (start+end)//2
            painters = self.isPossible(arr, k , mid)
            if(painters <= k):
                end  = mid-1
            else:
                start = mid+1
        return start
        # code here
        