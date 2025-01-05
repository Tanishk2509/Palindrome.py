def check_palindrome(str):
    rev = ''
    for char in str:
        rev = char+rev
    return rev
str = input(f'enter the character for check Palindrome: ')
reverse = check_palindrome(str)
if reverse == str:
    print(f'its palindrome')
else:
    print('its not Palindrome')
print(reverse,'its reverse of given character')