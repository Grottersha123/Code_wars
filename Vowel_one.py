"""vowelOne

Write a function that takes a string and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.

All non-vowels including non alpha characters (spaces,commas etc.) should be included.

Examples:
tests = [
    # [input, expected],
    ["vowelOne", "01010101"],
    ["123, arou", "000001011"],
    ["Codewars", "01010100"],
    ["Python", "000010"]
]
"""
def vowel_one(s):
    a = ''
    for i in s.lower():
        if i in 'aueuio':
            a+='1'
        else:
            a+='0'
    return a
