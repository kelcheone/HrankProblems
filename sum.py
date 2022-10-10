def series_sum(n):
    # Happy Coding ^_^
    denomAdd = 3
    sum = 1
    den_arr = []
    if n == 0:
        return "0.00"
    start = 1
    for num in range(1, (n)):
        start += denomAdd
        den_arr.append(start)

    for denom in den_arr:
        sum += 1/denom
    return '%.2f' % sum


print(series_sum(1))
