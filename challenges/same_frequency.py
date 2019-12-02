from collections import Counter


def same_frequency(n1, n2):
    s1, s2 = str(n1), str(n2)
    check1 = [True if s1[x] in s2 else False for x in range(len(s1))]
    check2 = [True if s2[y] in s1 else False for y in range(len(s2))]
    return True if all(check1) and all(check2) and len(check1) == len(check2) else False
    # d1, d2 = Counter(str(n1)), Counter(str(n2))
    # for key, value in d1.items():
    #     if not key in d2.keys() or len(str(n1)) != len(str(n2)):
    #         return False
    #     elif d1[key] != d2[key]:
    #         return False
    # return True


num1 = 1234978665
num2 = 432198756
print(same_frequency(num1, num2))

