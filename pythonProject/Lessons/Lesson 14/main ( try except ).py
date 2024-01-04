# try:
#     x = int(input("Ведіть число: "))
#     print("Ваш результат :", x * 2)
# except ValueError:
#     print("Ввести потрібно число, а не стрічку")
# ------------------------------------
# x = 0
# while x == 0:
#     try:
#         x = int(input("Ведіть число: "))
#         print("Ваш результат :", x * 2)
#     except ValueError:
#         print("Ввести потрібно число, а не стрічку")
#----------------------------------------------
try:
    x = 5 / 1
    x = int(input())
except ZeroDivisionError:
    print("Ви намагаєтесь ділити  на  - 0 -")
except ValueError:
    print('Ви написали не те')
else:
    print("else")
finally:
    print("Код виконано")
