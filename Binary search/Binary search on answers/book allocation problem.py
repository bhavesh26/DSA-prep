class Solution:
    
    def isPossible(self , arr , k , pages):
        count = 1
        currentPages = 0
        for page in arr:
            if(page+ currentPages <=pages):
                currentPages+=page
            else:
                count+=1
                currentPages = page
            
        return count
                
    
    
    
    
    def findPages(self, arr, k):
        start = max(arr)
        end = sum(arr)
        if k > len(arr):
            return -1
        while(start <=end):
            mid  = (start+end)//2
            student = self.isPossible(arr, k , mid)
            if(student<=k):
                end = mid-1
                
            else:
                start = mid+1
                
        return start
