num = input()
s = input()
e = input()
num, s, e = int(num), int(s), int(e)
m = (s+e)/2
if m ** 2 > num:
    while s < m:
        s += 0.00001
        if s ** 2 >= num or s >= m:
            break
    print(round(s, 3))
else:
    while e > m:
        m += 0.00001
        if m ** 2 >= num or m >= e:
            break
    print(round(m, 3))
