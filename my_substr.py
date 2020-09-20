def my_substr(string, length_sting):
    result_string = ''
    index = 0

    while index < length_sting:
        result_string = result_string + string[index]
        index = index + 1

    return result_string

print(my_substr('Kaznin', 4))