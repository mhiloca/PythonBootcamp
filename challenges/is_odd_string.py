def is_odd_string(string):
    # alpha = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8,
    #              i=9, j=10, k=11, l=12, m=13, n=14, o=15,
    #              p=16, q=17, r=18, s=19, t=20, u=21, v=22,
    #              w=23, x=24, y=25, z=26)
    # sum_up = 0
    # for letter in string.lower():
    #     sum_up += alpha[letter]
    sum_up = sum(ord(char) - 96 for char in string.lower())
    # return True if sum_up % 2 != 0 else False
    return sum_up % 2 == 1


text = 'Mhirley'
print(is_odd_string(text))
