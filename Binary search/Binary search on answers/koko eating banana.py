"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

"""
import math
def kokoEatingBanana(piles , h):
    def canFinish(piles, speed, h):
        hours = 0
        for pile in piles:
            hours+=math.ceil(pile/speed)
        return hours 

    left, right = 1, max(piles)
    ans = max(piles)
    while left <= right:
        mid = (left + right) // 2
        hrs = canFinish(piles, mid, h)
        if hrs<=h:
            ans = mid
            right = mid-1
        else:
            left = mid + 1
    return left

answer = kokoEatingBanana([3,6,7,11], 8)
print(answer)