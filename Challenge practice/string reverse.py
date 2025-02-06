def string_reverse(input):
    reverse_string = ''
    for input in input_variable:
        reverse_string = input + reverse_string
    return reverse_string
    


input_variable = input('Please enter a string: ')

print(f'reversed string is {string_reverse(input_variable)}')
