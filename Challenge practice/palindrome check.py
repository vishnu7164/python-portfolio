def palindrome_check(input_variable):
    reverse_input = input_variable[::-1]
    if reverse_input == input_variable:
        print('String is palindrome')
    else:
        print('String is not palindrome')

palindrome_input = input('Enter input values or text: ')

palindrome_check(palindrome_input)
