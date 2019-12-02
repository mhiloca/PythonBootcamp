def mode(nums):
    return max(nums, key=lambda a: nums.count(a))
    # for number in nums:
    #     if number not in new_nums.keys():
    #         new_nums = {number: 1}
    #     else:
    #         new_nums.update(number=nums.count(number))
    # return new_nums



numbers = [2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]
print(mode(numbers))
