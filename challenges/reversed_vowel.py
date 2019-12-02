# def reverse_vowels(string):
#     for letter in string:
#         if letter in 'aeiou':
#             string = reversed(string)
#     return string


text = 'aeiou'
vow = 'aeiouAEIOU'
vowels_text = [x for x in text if x in vow][::-1]
print(''.join(vowels_text.pop(0) if a in vow else a for a in text))

