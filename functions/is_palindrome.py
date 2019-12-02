def is_palindrome(msg):
    msg = msg.replace(" ", "").lower()
    if msg == msg[::-1]:
        return True
    return False


sent = input("Write a sentence: ")
print(is_palindrome(sent))
