# def max_magnitude(l):
#    return abs(max(l, key=lambda n: abs(n)))


def max_magnitude(l):
    return max(abs(n) for n in l)


def sum_even_values(*args):
    return sum(n for n in args if n % 2 == 0)


def interleave(s1, s2):
    return ''.join([''.join(t) for t in zip(s1, s2)])



num = [300, 20, -900]
print(max_magnitude(num))
soma = (sum_even_values(1, 2, 3, 4, 5, 6))
print(soma)

print('- ' * 15)
st1 = 'aaa'
st2 = 'zzz'
print(interleave(st1, st2))
print('- ' * 15)
nums = [1, 2, 3, 4, 5]
# new_nums = [n * 3 for n in nums if n % 4 == 0]
new_nums = list(
    map(lambda n: n * 3,
        filter(lambda x: x % 4 == 0, nums)
        )
)
print(new_nums)

print('- ' * 15)
names = [
    {'first': 'Elie', 'last': 'Schoppik'},
    {'first': 'Colt', 'last': 'Steele'}
]
# full_names = [f'{n["first"]} {n["last"]}' for n in names]
test = list(
    map(
        lambda n: ' '.join(n.values()), names
    )
)
print(test)


