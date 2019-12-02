def truncate(string, n):
    if n <= len(string):
        if n > 3:
            return f'{string[:n-3]}...'
        elif n < 3:
            return 'Truncation must be at least 3 characters'
        return '...'
    return string


text = 'Hello World'
print(truncate(text, 0))
