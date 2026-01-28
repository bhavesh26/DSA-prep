"""
Basic intution here and all binary search on answers are that i already know that answer will lie in a range ( sorted space)
the core logic here is not binary search this can also be done by simple loops
binary search is just used to optimize time 
"""

def nthroot(m, n):
    if n <2:
        return n
    start =1
    end = n
    ans =-1
    while(start<=end):
        mid  = (start+end)//2
        current = mid ** m
        if current ==n:
            return mid
        if(current < n):
            start = mid +1
        else:
            end = mid -1
    return -1
answer = nthroot(4,69)
print(answer)
            
        


