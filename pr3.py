#зд 1 возвращает фи/фио
def format_name(first_name, last_name, middle_name=None):
    if middle_name:
        return f"{last_name} {first_name} {middle_name}"
    return f"{last_name} {first_name}"

#зд 2 окальк
def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else None
    else:
        return None

#зд 3 кол-во + - 0 значений
def count_signs(numbers):
    positive = sum(1 for n in numbers if n > 0)
    negative = sum(1 for n in numbers if n < 0)
    zeros = sum(1 for n in numbers if n == 0)

    print(f"Положительных: {positive}")
    print(f"Отрицательных: {negative}")
    print(f"Нулей: {zeros}")

#зд 4 новы спис кажд эле преобрз функ transformer (делает функц гибкой)
def transform_list(numbers, transformer):
    return [transformer(n) for n in numbers]

#зд 5 сумм цифр полож целого числа n
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

#проверка работы этого чуда
if __name__ == "__main__":
    print("Задача 1: Форматирование ФИО")
    print(format_name("Артём", "Щейко"))
    print(format_name("Артём", "Щейко", "Романович"))

    print("\nЗадача 2: Калькулятор")
    print("10 + 5 =", calculate(10, 5, "+"))
    print("10 - 3 =", calculate(10, 3, "-"))
    print("4 * 7 =", calculate(4, 7, "*"))
    print("10 / 2 =", calculate(10, 2, "/"))
    print("10 / 0 =", calculate(10, 0, "/"))            # None

    print("\nЗадача 3: Анализ списка")
    count_signs([1, -2, 0, 3, -5, 0])

    print("\nЗадача 4: Преобразование списка")
    nums = [1, 2, 3, 4, 5]
    doubled = transform_list(nums, lambda x: x * 2)
    squared = transform_list(nums, lambda x: x ** 2)
    print("Исходник:", nums)
    print("Удвоенный:", doubled)
    print("Возведённый в кв:", squared)

    print("\nЗадача 5: Сумма цифр (рекурсия)")
    print("Сумма цифр числа 1234:", sum_digits(1234))   # 10
    print("Сумма цифр числа 5:", sum_digits(5))         # 5