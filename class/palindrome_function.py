def check_palindrome(enter_name: str):
    if enter_name == enter_name[::-1]:
        print("the word is a palindrome \N{smiling face with sunglasses}")
    else:
        print("the word is not a palindrome")


check_palindrome('mallam')