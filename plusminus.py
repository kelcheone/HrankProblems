def plusMinus(arr):
    l = len(arr)
    positives = 0
    negatives = 0
    zeros = 0
    for num in arr:
        if num > 0:
            positives += 1
        elif num == 0:
            zeros += 1
        else:
            negatives += 1
    prop_positive = f'{positives/l:.{6}f}'
    prop_negatives = f'{negatives/l:.{6}f}'
    prop_zeros = f'{zeros/l:.{6}f}'
    print(f'{prop_positive} \n')
    print(f'{prop_negatives}\n')
    print(f'{prop_zeros} \n')


plusMinus([-4, 3, -9, 0, 4, 1])
