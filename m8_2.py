def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        result, incorrect_data = personal_sum(numbers)
        if incorrect_data > 0:
            for number in numbers:
                if not isinstance(number, (int, float)):
                    print(f'Некорректный тип данных для подсчёта суммы - {number}')
        return result / len(numbers)
    except ZeroDivisionError:
        print("Ошибка: коллекция numbers пуста")
    except TypeError:
        print("В numbers записан некорректный тип данных")

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')