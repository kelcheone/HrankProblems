
def compareTriplets(a, b):
    # Write your code here
    points = [0, 0]
    for i in a:
        i -= 1
        # print(a[i], b[i])
        if a[i] > b[i]:
            points[0] += 1
        elif a[i] == b[i]:
            continue
        else:
            points[1] += 1
    return points


print(compareTriplets([5, 6, 7
                       ], [3, 2, 1]))
