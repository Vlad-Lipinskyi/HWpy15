# Створіть лямбда-функцію для обчислення куба числа.
print("Завдання 1")

n = int(input("Введіть число: "))
cube = lambda x: x**3
print(cube(n))

# Напишіть лямбда-функцію, яка перевіряє, чи є одне число кратним іншому, і перевірте її для різних пар чисел.
print()
print("Завдання 2")

isMultiple = lambda firstNumber, secondNumber: firstNumber % secondNumber == 0
print(isMultiple(10, 5))  
print(isMultiple(14, 3))  
print(isMultiple(21, 7))   
print(isMultiple(8, 2))    
print(isMultiple(9, 4))    


# Створіть лямбда-функцію для обчислення середнього арифметичного двох чисел.
print()
print("Завдання 3")

average = lambda a, b: (a + b) / 2
print(average(10, 4))  


# Напишіть лямбда-функцію для конвертації температури з Цельсія в Фаренгейт і навпаки. 
print()
print("Завдання 4")

celsiumToFarenheint = lambda c: (c * 9/5) + 32
farenheintToCelsium = lambda f: (f - 32) * 5/9

print(celsiumToFarenheint(0))    
print(celsiumToFarenheint(25))   

print(farenheintToCelsium(32))   
print(farenheintToCelsium(77))   


# Використовуючи теорему Піфагора, створіть лямбда-функцію для обчислення довжини гіпотенузи прямокутного трикутника за даними катетами. 
# a**2 + b**2 = c**2
print()
print("Завдання 5")
calculateTriangle = lambda a, b: (a**2 + b**2) ** 0.5

print(calculateTriangle(5, 7))

# Створіть лямбда-функцію для перевірки, чи є заданий рік високосним. Високосний рік ділиться на 4, але якщо він ділиться на 100, то має ділитися і на 400.
print()
print("Завдання 6")

isLeapYear = lambda year: (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

print(isLeapYear(2010))  
print(isLeapYear(1900))  
print(isLeapYear(2000))  
print(isLeapYear(2023))  


# Напишіть лямбда-функцію для визначення максимального з трьох чисел.
print()
print("Завдання 7")

maximumOfThree = lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)
print(maximumOfThree(3, 7, 5))   
print(maximumOfThree(10, 2, 10)) 
print(maximumOfThree(-1, -5, 0)) 