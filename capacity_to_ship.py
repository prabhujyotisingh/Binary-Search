def shipWithinDays(weights, days) -> int:
    n = len(weights)
    start, end = max(weights), sum(weights)

    def isValid(mx):
        day, sm = 1, 0
        for i in range(n):
            sm += weights[i]
            if sm > mx:
                day += 1
                sm = weights[i]
            if day > days:
                return False

        return True


    while start <= end:
        mid = start + (end - start) // 2

        if isValid(mid):
            end = mid - 1
        else:
            start = mid + 1

    return start