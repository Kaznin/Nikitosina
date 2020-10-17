def binary(number):
    number = abs(number) # только положительные
    result = [] # определяем список

    if number == 0:    # добавляем спец. условие для 0
        result.append(str(number))

    while number != 0:
        modulo = number % 2
        number = number // 2
        result.append(str(modulo))

    result.reverse()
    result = ''.join(result)
    return result


print(binary(100))
