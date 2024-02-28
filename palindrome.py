def is_palindrome(s):
    return s == s[::-1]

str = input("Enter your Word that you want to check:")

if is_palindrome(str) == True:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")