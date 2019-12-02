import termcolor as t
frase = input('What text do you want?')
cor = input('What color? ')
print(t.colored(frase, cor, attrs=['blink']))
