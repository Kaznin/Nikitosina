def is_neutral_soldier(color_armor, color_shield):
    return color_armor != 'red' and color_shield == 'black'

print(is_neutral_soldier('black', 'yellow'))