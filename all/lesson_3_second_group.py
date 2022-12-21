# -*- coding: utf-8 -*-
"""Lesson_3_second_group.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p4RlVt5Uo1gjmLGVwJcgRaXOuPROE3nv

## Boolean
"""

10 == 9

3 == 3

print(3 != 3)
print(3 > 2)
print(2 <= 3)

type(10 > 9)

bool('')

bool('False')

"""| True  | False |
| --- | -- |
| Більшість об'єктів | None |
| 1 | 0 |
| 3.4 | 0.0 |
| 'Будь-який текст' | '' |
"""

None

a = 3
print(3 < a)
print(a <= 5)
print(3 < a <= 5)

"""## Practice chapter 1:
1. Guess result of expression without executing it:

    a) 1 <= 1
    
    b) 1 != 1

    c) 1 != 2

2. Make all of them true.
    
    a) 3 __ 4

    b) 10 __ 5
    
    c) 42 __ "42"

## String
"""

print('Hello')
type('Hello')

print("Один великий рядок \
який може розтягнутись на декілька екранів\
")

print("""
Один великий рядок
який може розтягнутись на декілька екранів
""")

print('''
Один великий рядок
який може розтягнутись на декілька екранів
''')

print('"Apple" is doomed')

print("\"Apple\" is doomed")

print('Hellostudentsi`m a new string')
print('Hello\tstudents\ni`m a new string \\')

print(r"Hello\tstudents\ni\`m a new string \\")

"""## Practice chapter 2
1. Print the text in which there will be a quote with double quotes.
2. Print the text in which there will be an apostrophe.
3. Print one line that will be displayed on several lines
4. Print text that doesn`t fit in one line but will be displayed in one line
"""

print("Hello, " + "world" + '123')
type("Hello, " + "world")



'123' == "123"

str(123)

print('Value is ' + str(100))

print(str(2) + str(2))

print(2 + 2)

print("Львів " in "Київ, Львів, Харків, Одеса")
print("Львів," in "Київ, Львів, Харків, Одеса")

print("Київ" not in "Київ, Львів, Харків, Одеса")

print('Kyiv' == 'Kiev')

print('Kyiv' != 'Kiev')

print('Kyiv' > 'Kiev')

print('аб' > 'abb')

print('ab' > 'abc')

no = 'no' * 10
print(no)

yes = 'yes'
print(yes)

len(yes)

print(yes)
print(no)
len(yes) < len(no)

"""| y  | e | s |
| - | - | - |
| 0 | 1 | 2 |

"""

'yes'[2]

yes[3]

yes[0] + yes[1] + yes[2]

yes[0:2]

yes[:2]

yes[1:]

yes[:]

"""| y  | e | s |
| - | - | - |
| 0 | 1 | 2 |
| -3 | -2 | -1 |
"""

print(yes[-1])
print(yes[2])

yes *= 10

yes[:]

print(yes[:2] + yes[2:])

numbers = '123456789'

numbers[::2]

numbers[::-2]

numbers[-2:3:-2]

c = 'abc'

id(c)

c = c + 'd'
print(c)

id(c)

print(yes)
yes[2] = 'p'

yep = yes[:2] + 'p'
print(yep)
yes2 = yep[:2] + 's' 
print('yes2: ', yes2)

age = 'I`m 10 yearss old'

age.replace('10', '14')



"""## Practice chapter 3
1. Create a variable with data type string. Count the length of this line.
2. Create another variable with string data type. Output the result of concatenation of these two variables.
3. Print the two previous variables, but with a space between them.
4. Get a string from user input. Check if the string is a palindrome.
5. Replace age in the following string with your age. `"I'm 10 years old" -> "I'm 30 years old"`. Do it with  a) indexing and b) replace function. 
"""

birthday_str = 'I`m {age} years old. And my name is {name}'
current_age = 15
name_var = 'Peter'
print(birthday_str.format(name=name_var, age=current_age))

current_age = 15
name_var = 'Peter'
birthday_str = 'I`m {} years old. And my name is {}'
print(birthday_str.format(name_var, current_age))

age_1 = 11
new_name = 'Peter'
birthday_str = f'I`m {age_1} years old. And my name is {new_name}'

print(birthday_str)

print('forest gump'.upper())

"""## Practice chapter 4

1. The program receive user's name and age from input. Then you need to display the name and age in one line in several ways:

     a) by listing all the parameters in the print function

     b) by formatting a string using the format function

     c) by formatting a string with f-string

     String should looks like this: `"Your name is {name} and your {age} years old"`
"""

splitted = 'I`m split, years old'.split(' ')
print(splitted)

joined_str = '|'.join(splitted)
print((joined_str))

shitty_str = '   abc \n  '.strip()
print(shitty_str)

dir(str)

"""## Practice chapter 5
Format string with a proper functions

1. All letters must be written in lowercase.
```
string_1 = "Animals  "
```

2. All letters must be capitalized.
```
string_2 = "  Badger"
```

3. Remove all spaces:
```
string_3 = "   HoneyPot   "
```

   a) from the beginning of the line

   b) from the end of the line

   c) on both sides of the line

4. Check the value of the startwith ('Be') function for each line.:
```
string_1 = "Bear"
string_2 = "bear"
string_3 = "BEAR"
string_4 = "bEar"
```
Convert rows with methods from prev exercise to have positive result for each row.

```
formatted_string = string_1.some_cool_function()
formatted_string.startwith('Be')
> True
```

5. Find and replace all letters 's' with the letter 'x' in the following line: 
```
Somebody said something to Samantha.
```

6. Leave only numbers in the following line using only string methods: 
```
'12345!,_6--'
```

7. (Optional) Find a secret message in the following text: `'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'`

### Materials

#### Boolean
1. https://realpython.com/python-operators-expressions/#logical-operators

#### String 
1. https://realpython.com/python-strings/
2. https://realpython.com/python-string-formatting/
3. https://realpython.com/python-string-split-concatenate-join/
4. https://realpython.com/python-f-strings/
"""