def get_ean_auto():
    import random
    # от n_1 по n_7 определяем произвольные значения
    n_1 = random.randint(0, 9)
    n_2 = random.randint(0, 9)
    n_3 = random.randint(0, 9)
    n_4 = random.randint(0, 9)
    n_5 = random.randint(0, 9)
    n_6 = random.randint(0, 9)
    n_7 = random.randint(0, 9)

    # собираем все произольные значения с типом str
    EAN = str(n_1) + str(n_2) + str(n_3) + str(n_4) + str(n_5) + str(n_6) + str(n_7)

    # определяем ключ = n_8
    value_X = n_1 + n_3 + n_5 + n_7
    value_Y = n_2 + n_4 + n_6
    value_Z = value_Y + value_X * 3
    value_M = value_Z % 10

    if value_M == 0:
        value_M = value_M + 10
    else:
        value_M
    n_8 = 10 - int(value_M)

    return print(str(EAN) + str(n_8))

print(get_ean_auto())