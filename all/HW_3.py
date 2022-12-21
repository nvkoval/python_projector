
'''## Practice chapter 1:
1. Guess result of expression without executing it:

    a) 1 <= 1
        True
    b) 1 != 1
        False
    c) 1 != 2
        True

2. Make all of them true.

    a) 3 < 4

    b) 10 >= 5

    c) 42 != "42"
    '''

# String

# Practice chapter 2
# 1. Print the text in which there will be a quote with double quotes.
print('"Avatar" is a fantastic film')

# 2. Print the text in which there will be an apostrophe.
print('My name\'s Natalia')

# 3. Print one line that will be displayed on several lines
print('Hi! \nBye! \nGood luck!')
print('Hi!', 'Bye!', 'Good luck!', sep='\n')

# 4. Print text that doesn`t fit in one line but will be displayed in one line
print('Python is a very interesting \
 language')


# Practice chapter 3
# 1. Create a variable with data type string. Count the length of this line.
var_string = 'NoWar'
print(len(var_string))

# 2. Create another variable with string data type. Output the result of concatenation of these two variables.
another_var_string = 'inUkraine'
print(var_string + another_var_string)

# 3. Print the two previous variables, but with a space between them.
print(var_string + ' ' + another_var_string)
print(var_string, another_var_string)

# 4. Get a string from user input. Check if the string is a palindrome.
palindrome = input('Введіть слово-паліндром: ')
print(palindrome == palindrome[::-1])

# 5. Replace age in the following string with your age.
# `"I'm 10 years old" -> "I'm 30 years old"`.
# Do it with  a) indexing and b) replace function.
age = "I'm 10 years old"
print('with indexing:', age[:4] + '30' + age[6:])
print('replace metod:', age.replace('10', '30'))


# Practice chapter 4

# 1. The program receive user's name and age from input.
# Then you need to display the name and age in one line in several ways:
# String should looks like this: `"Your name is {name} and your {age} years old"`
name, age = input('Введіть ім\'я: '), input('Введіть вік: ')

#   a) by listing all the parameters in the print function
print('A:', 'Your name is', name, 'and your', age, 'years old')

#   b) by formatting a string using the format function
print('B:', 'Your name is {name} and your {age} years old'.format(name=name, age=age))
print('B:', 'Your name is {} and your {} years old'.format(name, age))

#   c) by formatting a string with f-string
print('C:', f'Your name is {name} and your {age} years old')


# Practice chapter 5
# Format string with a proper functions

# 1. All letters must be written in lowercase.
string_1 = "Animals  "
print(string_1.lower())

# 2. All letters must be capitalized.
string_2 = "  Badger"
print(string_2.upper())

# 3. Remove all spaces:
string_3 = "   HoneyPot   "

#   a) from the beginning of the line
print(string_3.lstrip())

#   b) from the end of the line
print(string_3.rstrip())

#   c) on both sides of the line
print(string_3.replace(' ', ''))
print(string_3.strip())

# 4. Check the value of the startwith ('Be') function for each line.:
string_1 = "Bear"
string_2 = "bear"
string_3 = "BEAR"
string_4 = "bEar"
print(string_1.startswith('Be'))
print(string_2.startswith('Be'))
print(string_3.startswith('Be'))
print(string_4.startswith('Be'))

# Convert rows with methods from prev exercise to have positive result for each row.
formatted_string_1 = string_1.capitalize()
print(formatted_string_1.startswith('Be'))

formatted_string_2 = string_2.capitalize()
print(formatted_string_2.startswith('Be'))

formatted_string_3 = string_3.capitalize()
print(formatted_string_3.startswith('Be'))

formatted_string_4 = string_4.capitalize()
print(formatted_string_4.startswith('Be'))

# 5. Find and replace all letters 's' with the letter 'x' in the following line:
line = 'Somebody said something to Samantha.'
print(line.replace('s', 'x'))

# 6. Leave only numbers in the following line using only string methods:
line = '12345!,_6--'
line_1 = line.strip('-')
line_2 = line_1.replace('!,_', '')
print(line_2)

# 7. (Optional) Find a secret message in the following text: `'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'`
text = 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'
print(text)
print((text.replace('X', '')).replace('x', '')[::-1])
# Out: It`s a secret line!
