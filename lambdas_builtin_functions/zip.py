num1 = [0, 1, 2, 3, 4]
num2 = [n * 2 for n in num1]
num = list(zip(num1, num2))
print(num)
n1 = list(zip(*num))
print(n1)
n2 = dict(zip(num1, num2))
print(n2)

st1 = 'Mhiloca'
st2 = 'Cabezita'
st = list(zip(st1, st2))
print(st)
print('- ' * 15)
st_final = []
for i in st:
    for x in i:
        st_final.append(x)
print(st_final)

midterms = [80, 91, 73]
finals = [98, 89, 58]
stu = ['kate', 'dan', 'angela']

final_grades = {t[0]: max(t[1], t[2]) for t in zip(stu, midterms, finals)}

scores = list(zip(
    stu, map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
))
print(final_grades)
print(scores)
print('- ' * 15)
avg_grades = {
    t[0]: (t[1] + t[2]) / 2 for t in zip(
        stu, midterms, finals
    )
}
print(avg_grades)
average = dict(
    zip(
        stu, map(
            lambda grade: (grade[0] + grade[1]) / 2,
            zip(midterms, finals)
        )
    )
)
print(average)