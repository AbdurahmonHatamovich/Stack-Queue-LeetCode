def is_palindrome(x):
    x_str = str(x)

    return x_str == x_str[::-1]


x = 121
print(is_palindrome(x))

x = 123
print(is_palindrome(x))
