# --- Умови та цикли ---

# range(індекс початку, індекс закінчення, крок)
#-----------------------------
# for i in range(7):
#     if i > 0:
#        print(i)

# ----------------------------
# for i in range(2, 7):
#     print(i)
#
# ----------------------------
# for i in range(1, 20, 2):
#     print(i)

# ----------------------------
# for i in "Hello world":
#     print(i)
# ----------------------------
# word = "Hello world"
#
# for i in word:
#     print(i)
#
# ----------------------------
# word = "Hello world"
#
# for i in word:
#     print(i*3)
# # ----------------------------
# count = 0
# word = "Hello world !"
#
# for i in word:
#     if i == "o":
#         count += 1
# print("count = ", str(count))
#------------------------------
# i = 5
# while i <= 15:
#     print(i)
#     i += 2
#-----------------------------
# logOut = True
# userPassword = 258
# UserLogin = "ivan"
#
# while logOut:
#     if (int(input("Enter password: ")) == userPassword
#         and input("Enter login: ") == UserLogin):
#             logOut = False
#             print("you have successfully logged in")
#     else:
#         print("you are not logged in")

#----------------------------------
for i in range(1, 11):
    if i >= 10:
        break
# i % 2 --- ділення на 2 без дробових результатів
    if i %  2 == 0:
        continue
    print(i)
#-------------------------------------
# found= None
# for i in "hello":
#
#     if i == "l":
#         found = True
#         break
# else:
#     found = False
# print(found)