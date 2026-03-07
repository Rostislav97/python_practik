
def is_palindrome(word):
    if word == word[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")



is_palindrome("океан")