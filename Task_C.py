def input_many_int_vals():
    return [int(num) for num in input().split()]


list_length, n = input_many_int_vals()
nums = list(set(input_many_int_vals()))
maxes = []
if n > len(nums):
    print("-1")
else:
    for i in range(n):
        maximum = max(nums)
        nums.remove(maximum)
        maxes.append(maximum)
    print(maxes[n-1])
    