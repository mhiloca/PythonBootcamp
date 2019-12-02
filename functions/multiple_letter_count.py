def multiple_letter_count(msg):
    return {char: msg.count(char) for char in msg}


sent = input("Write a sentence: ")
print(multiple_letter_count(sent))
