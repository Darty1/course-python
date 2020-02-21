# coding=utf-8
import re

letters = {
    'а': '00000',
    'б': '00001',
    'в': '00010',
    'г': '00011',
    'д': '00100',
    'е': '00101',
    'ж': '00110',
    'з': '00111',
    'и': '01000',
    'й': '01001',
    'к': '01010',
    'л': '01011',
    'м': '01100',
    'н': '01101',
    'о': '01110',
    'п': '01111',
    'р': '10000',
    'с': '10001',
    'т': '10010',
    'у': '10011',
    'ф': '10100',
    'х': '10101',
    'ц': '10110',
    'ч': '10111',
    'ш': '11000',
    'щ': '11001',
    'ъ': '11010',
    'ы': '11011',
    'ь': '11100',
    'э': '11101',
    'ю': '11110',
    'я': '11111',
    ' ': ''
}
dec = {
    '00000': 0,
    '00001': 1,
    '00010': 2,
    '00011': 3,
    '00100': 4,
    '00101': 5,
    '00110': 6,
    '00111': 7,
    '01000': 8,
    '01001': 9,
    '01010': 10,
    '01011': 11,
    '01100': 12,
    '01101': 13,
    '01110': 14,
    '01111': 15,
    '10000': 16,
    '10001': 17,
    '10010': 18,
    '10011': 19,
    '10100': 20,
    '10101': 21,
    '10110': 22,
    '10111': 23,
    '11000': 24,
    '11001': 25,
    '11010': 26,
    '11011': 27,
    '11100': 28,
    '11101': 29,
    '11110': 30,
    '11111': 31,
    '': ' ',
}
# key_i = str(input("input key: "))
# word_i = str(input("input word: "))
key_i = 'лондон'
word_i = 'пальмал ама'
word_i.replace(' ', '')
print(word_i)
key = []
word = []
for k in key_i:
    key.append(letters[k])
for w in word_i:
    word.append(letters[w])

print('key: ', key)
print('wor: ', word)


def addition(w, k):
    binary_coding = []
    n = 0
    l = 0
    for i in range(len(w)):
        c = ''
        n = 0
        for j in w[i]:
            if l == len(k):
                l = 0
            if j == k[l][n]:
                c += '0'
            else:
                c += '1'
            n += 1
        l += 1
        binary_coding.append(c)
    return binary_coding


dec_coding = []
binary_coding = addition(word, key)
print('cod: ', binary_coding)

for c in binary_coding:
    dec_coding.append(dec[c])

print('dec: ', dec_coding)

dec_encoding = addition(binary_coding, key)

print('enc: ', dec_encoding)
