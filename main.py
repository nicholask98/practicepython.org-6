'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

user_string = input('Enter word to test if it is a palindrome:\n')

is_pal = True

for x in range(0, len(user_string)):
    if user_string[x].lower() != user_string[-x - 1].lower():
        is_pal = False
        break


if is_pal == True:
    print('{} is a palendrome'.format(user_string))
else:
    print('{} is not a palendrome'.format(user_string))