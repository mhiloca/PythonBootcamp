msg_inicial = input()
msg_inicial = msg_inicial.split()
tam, msg = int(msg_inicial[0]), msg_inicial[1]
possibilidades = []
for i in range(len(msg)-tam):
    teste = []
    letter = i
    c = 0
    while c < tam:
        teste.append(msg[letter])
        letter += 1
        c += 1
    possibilidades.append(''.join(teste))
print(max(possibilidades, key=lambda a: possibilidades.count(a)))
