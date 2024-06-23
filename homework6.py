my_dict = { 'Vasya': 1975, 'Egor': 1999, 'Masha':2002}

print("Dict:", my_dict)

existing_value = my_dict.get('Masha')
print("Existing value:",existing_value)

not_existing_value = my_dict.get('Ivan')
print("Not existing value:", not_existing_value)

my_dict['Kamila'] = 1981
my_dict['Artem'] = 1915

deleted_value = my_dict.pop('Egor')
print("Deleted value:", deleted_value)

print("Modified dicionary:", my_dict)

my_set = {1,'яблоко', 42.314,'яблоко', 1,}

print("Set:", my_set)

my_set.add(13)
my_set.add((5,6,1.6))

my_set.remove(1)

print("Modified set:",my_set)