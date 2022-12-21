# Task 1. Дискримінант. Створіть функцію з іменем discriminant.
# Функція повинна приймати на вхід a, b, c, choose. Де a, b, c - це аргументи функції, choose - опціональний параметр, вибору способу рішення(дискримінант або Вієта, 1 - disc, 2 - Вієта)
# Функція повинна повертати в залежності від параметрів один/два кореня або їх відсутність.

# Example:
# Input: a = 5, b = -8, c = 3
# Output: x = 1, x = 0.6 Результати округлювати до 2 знаку. Функція повинна перевіряти тип аргументів(int повинен бути).

# Крок 1: допустимі типи, isinstance, type, [int, float, bool]
# Крок 2: Ділення на 0, etc....
# Крок 3: без бібліотек!!!!
# Крок 4: Оптимальність 
# Крок 5: перевірка назв 
# Крок 6: побітові операції + винагорода 
# Крок 7: Обмеженна 3 ступені
# Крок 8: тільки цикли, функції, строки-числа, built-in-function(sum, len) можна

def discriminant(a: int, b: int, c: int, choose = 1):

    # розв'язання через дискриминант        
    def disc():
        D = b**2 - 4*a*c
        print(f'D = {D}')

        if D > 0:
            x1 = (-b - D**0.5) / (2*a)
            x2 = (-b + D**0.5) / (2*a)
            result = f'x1 = {round(x1, 2)}, x2 = {round(x2, 2)}'
            return result
        elif D == 0:
            x = -b / (2*a)
            result = f'x1 = x2 = {round(x, 2)}'
            return result
        else: 
            result = 'Дійсних коренів немає, D < 0'
            return result

    # роз'язання за допомогою теореми Вієта        
    def viet():
        mult_x = c / a
        sum_x = -b / a
        x0 = -b / (2 * a)
        x1 = x2 = round(x0, 5)
        if b**2 - 4*a*c >= 0:
            while (round(x1 * x2, 3) != round(mult_x, 3)):
                x1 = round(x1 - 0.001, 3)
                x2 = round(x2 + 0.001, 3) 
            result = f'x1 = {round(x1, 2)}, x2 = {round(x2, 2)}'
        else: result = 'Дійсних коренів немає'
        return result 

    # перевірка типів введених даних
    if isinstance(a, (int, float, bool)) and isinstance(b, (int, float, bool)) and isinstance(c, (int, float, bool)): 
        
        # виключення ділення на нуль 
        if a == 0 :  
            return 'а = 0, це не квадратне рівняння'
        else:

            # відповідного до введеного параметру choose розв'язуємо або дискриминантом, або за теоремою Вієта
            match choose:
                case 1: 
                    return disc()
                case 2: 
                    return viet()
                case _: 
                    return 'Bad input'
    else: return 'Bad input'


print(discriminant(5, -8, 3))
print(discriminant(5, -8, 3, choose = 2))
print('='*10)

print(discriminant(1, 4, 4))
print(discriminant(1, 4, 4, choose = 2))
print('='*10)

print(discriminant(1, 2, 4))
print(discriminant(1, 2, 4, choose = 2))
print('='*10)

print(discriminant(0, 1, 3))
print(discriminant(0, 1, 3, choose = 2))
print('='*10)

print(discriminant(1, -2, -24))
print(discriminant(1, -2, -24, choose = 2))
print('='*10)

print(discriminant(1, -13, 12))
print(discriminant(1, -13, 12, choose = 2))
print('='*10)

print(discriminant(1, -15, 26))
print(discriminant(1, -15, 26, choose = 2))
print('='*10)
