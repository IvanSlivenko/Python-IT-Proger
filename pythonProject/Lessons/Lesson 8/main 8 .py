# ------------- Зрізи ---------
# word ="itprogger"
# print("word", word)
# print("word[1]", word[1])
#
# print("word", word)
# print("len(word)", len(word))
# ----------------------------------------------------Рахуємо кількість символів
# print("word", word)
# print("word.count('g')", word.count('g'))
#---------------------------------------------------- Переводимо у верхній регістр
# print("word", word)
# print("word.upper()", word.upper())
#
# print("word", word)
#------------------------------------------------------Переводимо у нижній регістр
# uperWord = word.upper()
# print("uperWord", uperWord)
# print("uperWord.lower()", uperWord.lower())
#

# False or True
# print("word", word)
# print("word.isupper()", word.isupper())

# False or True
# print("word", word)
# print("word.islower()", word.islower())
#
# print("word", word)
# print("word.capitalize()", word.capitalize())
#
# --------------------------------------------------Захуємо - скільки разів зустрічається символ
# print("word", word)
# print("word.find(\"p\")", word.find("p"))

# wordTwo = "Footbal, basketball, skate"
# print("wordTwo ", wordTwo)

# --------------------------------------------------Переводимо стрічку у список
# hobby = wordTwo.split(', ')
# print("wordTwo.split(',')", hobby)
# print("hobby[1]", hobby[1])
#
# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()
#
# print("hobby", hobby)
#
# -------------------------------------------------Переводимо список у стрічку
# result = ", ".join(hobby)
# print("result = ", ".join(hobby) = ", result)
#-------------------------------------------------
#------------------- index -----------------------

# newWord = "Football"
# res = newWord[4:int(len(newWord))]
# print("res", res)
#
# newWord = "Football"
# res = newWord[4:]
# print("res", res)
#
# newWord = "Football"
# res = newWord[4:-1]
# print("res", res)

lis = [6,4,"Strichka", True, 6.5]

print("reslist", lis[2:])
print("reslist", lis[2:5])
print("reslist", lis[2:-1])
print("reslist", lis[2:-2])
print("reslist", lis[::])
print("reslist", lis[::-1])







