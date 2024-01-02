# Lesson 10
# Словники

# Step 1
# ---------------------------
# country = {'Name': 'Ivan'}
# print(country['Name'])
# ----------------------------
# Variant 2
# -------------------------------
# country = dict(
#     code='UA',
#     name='Ukraine',
#     population=42
# )
# print(country['name'])
# ---------------------------------------

# Variant 1
# ------------------------
# country = {'code': 'UA',
#            'name': 'Ukraine',
#            'population': 42,
#            'language': 'Ukrainian'
#            }


# ---------------------------------------
# ----------------------------------------
# country.clear()
country = {'code': 'UA',
           'name': 'Ukraine',
           'population': 42,
           'language': 'Ukrainian'
           }
# переглядаємо структуру Словника country
# print(country)
# print(country.items())

#Перебираємо словник у циклі
# for key, value in country.items():
#     print(key, " - ", value)

#Очищаємо весь словник
# country.clear()

# видаляємо елемент словника за назвою ключа
# country.pop('population')

# видаляємо останній елемент словника
# country.popitem()
# print(country)

#Отримуємо елемент за назвою ключа
# print(country['language'])
# print(country.get('language'))
#
# #Отримуємо перелік ключів
# print(country)
# print(country.keys())
#
# # отримуємо перелік значень Словника
# print(country.values())
#
# # Отримуємо перелік Ключів та значень
# print(country.items())
#
# # Змінюємо значення змінної за ключем
# country['code'] = 'None'
# print(country.items())

# ------------------------------------

person = {
    'user_1': {
        'first_name' : 'John',
        'last_name' : 'Marley',
        'age': 45,
        'address': ('м. Київ', 'вул. Енергетиків', '45'),
        'grages': {
            'math': 5,
            'physics': 5,
            'music': 4
        }

    },
    'user_2': {
        'first_name' : 'Ivan',
        'last_name' : 'Slivenko',
        'age': 42,
        'address': ('м. Умань', 'вул. ІІІ - тя Східна', '19'),
        'grages': {
            'math': 4,
            'physics': 5,
            'music': 5
        }

    }
}

# отримуємо значення зі словника
print(person['user_1']['address'])
print(person['user_2']['address'])
print(person['user_1']['address'][1])
print(person['user_2']['address'][1])








