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
country = {'code': 'UA',
           'name': 'Ukraine',
           'population': 42,
           'language': 'Ukrainian'
           }

# print(country['language'])
# print(country)
# ---------------------------------------
# for key, value in country.items():
#     print(key, " - ", value)
# ----------------------------------------
# country.clear()
print(country.get('name'))
print(country)
# видаляємо елемент словника
country.pop('population')
# видаляємо останній елемент словника
country.popitem()
print(country)
