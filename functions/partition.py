def is_even(num):
    return num % 2 == 0


def partition(lis, is_even):
    return [[val for val in lis if is_even(val)], [n for n in lis if not is_even(n)]]


nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(partition(nums, is_even))
