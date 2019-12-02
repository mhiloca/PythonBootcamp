from pyfiglet import figlet_format as fig
import termcolor as t

texto = input('What text do you want to write? ')
cor = input('What color? ')
try:
    print(t.colored(fig(texto), cor, attrs=['blink']))
except KeyError:
    print(t.colored(fig(texto), color='blue'))
