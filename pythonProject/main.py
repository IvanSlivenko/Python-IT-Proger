# try:
#     x = int(input("Ведіть число: "))
#     print("Ваш результат :", x * 2)
# except ValueError:
#     print("Ввести потрібно число, а не стрічку")
# ------------------------------------
x = 0
while x == 0:
    try:
        x = int(input("Ведіть число: "))
        print("Ваш результат :", x * 2)
    except ValueError:
        print("Ввести потрібно число, а не стрічку")
