def multiple_of5(nums):
    fmarks = []
    for num in nums:
        fin = 5 * round(num/5)
        # Check the difference
        diff = (fin - num)

        if diff < 38:
            fmarks.append(num)
        else:
            fmarks.append(fin)
        # Generate grades

    return fmarks


nums = [73, 67, 38, 33]
print(multiple_of5(nums))

print((round(33/5)))


def gradingStudents(grades):
    # Write your code here
    fmarks = []
    for num in grades:
        fin = 5 * round(num/5)
        # Check the difference
        diff = (fin - num)

        if diff < 3 and num >= 38 and diff != 0:
            fmarks.append(fin)
        else:
            fmarks.append(num)
