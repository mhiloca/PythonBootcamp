def go_on(msg):
    while True:
        ans = input(f'Would you like to register another {msg}? ').strip().upper()[0]
        if ans not in 'NY':
            print('\033[31mInvalid answer\033[m')
        else:
            return ans


def play():
    while True:
        ans = input('Would you like to play again? ').strip().upper()[0]
        if ans not in 'NY':
            print('\033[31mInvalid answer\033[m')
        else:
            return ans
