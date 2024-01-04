#------------------------------------------
# try:
#     file = open('files/text1.text', 'r')
#     print(file.read())
#
#     file.close()
# except FileNotFoundError:
#     print('файл для відкриття  не знайдено')
#--------------------------------------------------
try:
    file = open('files/text1.text', 'r')
    print(file.read())

    file.close()
except FileNotFoundError:
    print('файл для відкриття  не знайдено')
