def minDays(bloomDay, m, k) -> int:
    n = len(bloomDay)
    if n < m * k:
        return -1

    start, end = min(bloomDay), max(bloomDay)
    res = -1

    def canMakeBoquet(mx):
        count, num_of_boquets = 0, 0
        for day in bloomDay:
            if day <= mx:
                count += 1
            else:
                count = 0

            if count == k:
                num_of_boquets += 1
                count = 0

            if num_of_boquets == m:
                return True

        return False

    while start <= end:
        mid = start + (end - start) // 2
        
        if canMakeBoquet(mid):
            end = mid - 1
            res = mid
        else:
            start = mid + 1

    return res
