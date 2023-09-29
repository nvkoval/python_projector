'''
Теоретична частина
1. Наведіть програмний приклад логічної та синтаксичної помилки.
    Логічна помилка - код працює, але повертає неправильний результат.
        user_id = 54120
        e_mail = str(user_id) + '@i.com'
        print ('e-mail', user_id)
    Синтаксична помилка - намагаємося виконати код, якого немає зарезервованого в системі, або виконати дію, яка не прописана.
        flaot(8.5)
            Помилка в написанні команди

2. Який буде результат при 1 / 0, 0 / 1 - зафіксувати його та пояснити.
    При 1/0 буде помилка стосовно ділення на нуль, бо ділити на нуль не можна
        print(1/0)
        out: ZeroDivisionError: division by zero

    При 0/1 буду відповідь 0. При ділення нуля на будь-яке число, окрім нуля, отримаємо нуль.
        print(0/1)
        out: 0.0

3. Навіщо потрібні коментарі?
    Для пояснення, що відбувається у коді.

4. Що таке змінна?
    Змінна - область пам'яті, яка має ім'я (іменована ячейка пам'яті).
    Характеристика змінної:
        1. Область допустимих значень.
        2. Діапазон допустимих операцій.
        3. Кількість пам'яті, яку займає.
'''

# Практична частина

# 1. Написати програму яка отримує від користувача два числа. Вивести ці два числа в консоль
num_one, num_two = int(input('Enter number one: a = ')), int(input('Enter number two: b = '))
print('a = ', num_one, ', b = ', num_two)

# 2. Провести та вивезти над ними всі базові арифметичні операції в print
plus = num_one + num_two  # Plus value
diff = num_one - num_two  # Minus value
mult = num_one * num_two  # Multi value
print('a + b = ', plus)
print('a - b = ', diff)
print('a * b = ', mult)

# 3. Додати функціонал по знаходженню степені числа. Перше число є базою, друге - ступенем. Вивести результат в консоль у форматі "а в b степені це c»
power_value = num_one ** num_two
print('a в степені b (a ^ b) це ', power_value)

# 4. Додати можливість працювати зі float
num_one, num_two = float(input('Enter number one: a = ')), float(input('Enter number two: b = '))
print('a = ', num_one, ', b = ', num_two)
plus = num_one + num_two  # Plus value
diff = num_one - num_two  # Minus value
mult = num_one * num_two  # Multi value
print('a + b = ', plus)
print('a - b = ', diff)
print('a * b = ', mult)

# 5. Прийняти від користувача ім'я, призвіще, вік, вивезти одним print:
# Name Surname
# You are, вік , years old
name, surname, age = input("Введить ім'я: "), input("Введить прізвище: "), input("Введить свій вік: ")
print(name + ' ' + surname + '\n' + 'You are ' + age + ' years old')
