get_ean8 = input('Input 7 numbers: ')

value_X = int(get_ean8[0]) + int(get_ean8[2]) + int(get_ean8[4]) + int(get_ean8[6])
value_Y = int(get_ean8[1]) + int(get_ean8[3]) + int(get_ean8[5])
value_Z = value_Y + value_X * 3
value_M = value_Z % 10

if value_M == 0:
    value_M = value_M + 10
else:
    value_M
CkeckSum = 10 - int(value_M)

# выводим на печать
print(str(get_ean8) + str(CkeckSum))
