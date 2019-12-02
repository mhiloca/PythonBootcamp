from collections import Counter


def mode(nums):
    new_nums = Counter(nums).most_common()
    return new_nums[0][0]


num = [2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]
print(mode(num))