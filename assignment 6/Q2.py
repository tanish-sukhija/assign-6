def is_palindrome():
    string = input("Enter a string: ")
    if string == string[::-1]:
        print(string," is a palindrome.")
    else:
        print(string," is not a palindrome.")

is_palindrome()