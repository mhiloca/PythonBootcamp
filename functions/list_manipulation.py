def list_manipulation(lis, com, loc, value=None):
    if com == "remove":
        if loc == "beginning":
            return lis.pop(0)
        return lis.pop()
    elif com == "add":
        if loc == "beginning":
            lis.insert(0, value)
            return lis
        lis.append(value)
        return lis


nums = [1, 2, 3, 4]
print(list_manipulation(nums, "add", "beginning", 88))
