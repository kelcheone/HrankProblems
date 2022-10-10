def staircase(n):
    for i in range(1, n+1):
        # print(" "*(n-i) + "#"*i)
        print('#'*i + ' '*(n-i))


staircase(6)
