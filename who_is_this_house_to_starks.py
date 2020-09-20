def who_is_this_house_to_starks(family):
    if family == 'Karstark' or family == 'Tully':
        return 'friend'
    elif family == 'Lannister' or family == 'Frey':
        return  'enemy'
    else:
        return 'neutral'

print(who_is_this_house_to_starks('Frey'))