def minEatingSpeed(piles, h) -> int:
    n = len(piles)
    start, end = 1, max(piles)

    def canEat(mx):
        hrs = 0
        for i in range(n):
            hrs += piles[i] // mx
            if piles[i] % mx != 0:
                hrs += 1

            if hrs > h:
                return False

        return True

    while start <= end:
        mid = start + (end - start) // 2

        if canEat(mid):
            end = mid - 1

        else:
            start = mid + 1

    return start