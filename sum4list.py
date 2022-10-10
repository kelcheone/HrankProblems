def summArr(arr):
    sum1 = 0
    sum2 = 0
    for i in range(1, len(arr)):
        sum1 += sorted(arr, reverse=False)[i]
    for i in range(1, len(arr)):
        sum2 += sorted(arr, reverse=True)[i]
    print(f'{sum1} {sum2}')


def get_max(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return arr.count(max)


print(get_max([10, 2, 3, 10, 5, 6, 7, 8, 9, 10]))

# summArr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
