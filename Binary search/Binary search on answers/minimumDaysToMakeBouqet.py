class Solution:


    def isPossible(self,day , bloomDay , m , k):
        flow = 0
        bouq = 0
        for b in bloomDay:
            if b<=day:
                flow+=1
                if(flow==k):
                    bouq+=1
                    flow=0
            else:
                flow =0
        return bouq>=m
        
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        low, high = min(bloomDay), max(bloomDay)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if self.isPossible(mid, bloomDay, m, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
        