'''print(round(10 / 3, 2),  # Не ціле ділення + округлення результата
      10 // 3,
     10 % 3) # Ціло ділення, відкидуємо математично дробну частину'''

'''a, b = int(input('Enter number one: a = ')), int(input('Enter number two: b = '))
print('a = ', a, ', b = ', b)

tsila_chast = a // b 
ostacha = a - b * tsila_chast
print(ostacha)'''

'''hour_in_day = 24
min_in_hour = 60
sec_in_min = 60
day_in_year = 365
year = 1
day = 1
sec_day = day * hour_in_day * min_in_hour * sec_in_min
print(sec_day)

sec_year = year * day_in_year * sec_day
print(sec_year)'''

'''# Bool type
a, b = True, False # Or equal 1, 0 
print(a, b, int(a), bool(int(b) - 10))

print(bool(1 - 1), bool(1 - 2), bool(1 + 10), sep = '\n')

print(type(a+1))'''

'''print(3 < 4)
print(10 > 5) 
print(42 != "42")'''

'''# Оператор екранування(\) - вказуємо що це та сама строка 
print("Один великий рядок \
який може розтягнутись на декілька екранів\
")'''

'''print("""
Один великий рядок
який може розтягнутись 
на декілька екранів
""")'''

'''print("'Apple' is doomed")
print('"Apple" is doomed')
print("\"Apple\" is doomed")

print('Hellostudentsi`m a new string')
print('Hello\tstudents\ni`m a new string \\')
print('a\tc')'''


'''string = 'Hello World!'
print(string, type(string))'''

'''print(r'Hello\tstudents\ni`m a new string \\')'''

'''print(str(2) + str(2), 2 + 2 , sep = '\n')'''

'''print("Львів " in "Київ, Львів, Харків, Одеса")
print("Львів," in "Київ, Львів, Харків, Одеса")

print("Київ" not in "Київ, Львів, Харків, Одеса")'''

'''print('a' * 10)'''
'''a = 'ashsa'
print(a == a[::-1])'''

name, surname, age = input("Введить ім'я: "), input("Введить прізвище: "), input("Введить свій вік: ")
print (name + ' ' + surname + '\n' + 'You are ' + age + ' years old')

print('abc' < 'fgr')

string = '123456'
print(string[4::-1])