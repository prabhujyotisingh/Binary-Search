def splitArray(arr, k) -> int:
    n = len(arr)
    start = max(arr)
    end = sum(arr)
    res = -1

    def isValid(mx):
        arrays, sm = 1, 0
        for i in range(n):
            sm += arr[i]
            if sm > mx:
                arrays += 1
                sm = arr[i]
            if arrays > k:
                return False

        return True

    while start <= end:
        mid = start + (end - start) // 2

        if isValid(mid):
            res = mid
            end = mid - 1
        
        else:
            start = mid + 1

    return res

