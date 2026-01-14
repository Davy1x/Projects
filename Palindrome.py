#PALINDROME IN PYTHON

my_list = [
    'mummy',
    'hannah',
    'murder for a jar of red rum',
    'mom',
    'seagull',
    'tomato',
    'no lemon',
    'no melon',
    'some men interpret nine memos',
    'madam',
    'david',
    'fred',
    'bob'
]

# REMOVE TRAILING AND INLINE WHITESPACES
def clearWhiteSpace():
    arr = []
    for chars in my_list:
        x = ''.join(chars.split(' '))
        arr.append(x)
    return arr

# LOOP THROUGH THE RETURNED ARRAY 
for chars in clearWhiteSpace():
    x = []
    for ch in chars:
        x.insert(0, ch)
    if chars == ''.join(x):
        print(f"{my_list[clearWhiteSpace().index(chars)]}: \033[33m Is Palindromic \033[0m")
    else:
        print(f"{my_list[clearWhiteSpace().index(chars)]}: \033[31m Is Not Palindromic \033[0m")



# FOR MORE INFORMATION CONCERNING THIS PROJECT OR REPO - LOCATE THE README.mb FILE