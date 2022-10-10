def veryBigSum(arr):
    sum = 0
    for num in arr:
        sum += num

    return sum


print(veryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))
