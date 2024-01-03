# ---------------------------pass === нічого

# def test_func():
#     pass
#
# test_func()
# -------------------------------------------
# def test_func(word):
#     print(word, end="")
#     print("!")
#
# test_func("Hi")
# #--------------------------------------------
# def summa(a,b):
#     res = a + b
#     print("Result:", res)
#
# summa(5, 7 )
# summa("H", "i")
# summa(str(5), "i")
# -----------------------------------------------
# def summa(a,b):
#     res = a + b
#     return res
#
# resTwo = summa(5, 7)
# print(resTwo)
#--------------------------------------------------
# def summa(a, b):
#     return a + b
#
# resTwo = summa(5, 7)
# print(resTwo)
#-------------------------------------------------
# def summa(a, b):
#     return a + b
#
# summa(5, 7)
# print(summa(5, 7))
#------------------------------------------------
#------------------------------------------------Шукаємо мінімальний елемент у списку
# nums = [5, 7, 2,  9, 4]
# min= nums[0]
#
# for el in nums:
#     if el < min:
#         min = el
#
# print(min)

#-----------------------------------
# nums2 = [5.1, 7.5, 2.1,  9.4, 4.6]
# min2= nums2[0]
#
# for el in nums2:
#     if el < min2:
#         min2 = el
#
# print(min2)
#--------------------------------------------- Стандартизуємо функцію
# def minimal(l):
#     min_number = l[0]
#     for el in l:
#         if el < min_number:
#             min_number = el
#
#     # print(min_number)
#     return min_number
# def maximal(l):
#     max_number=l[0]
#     for el in l:
#         if el > max_number:
#             max_number = el
#     # print(max_number)
#     return  max_number
#
#
# nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
# min1 = minimal(nums1)
# max1 = maximal(nums1)
#
# nums2 = [3, 4, 5, 6, 7, 8]
# min2 = minimal(nums2)
# max2 = maximal(nums2)
#
# if min1 < min2:
#     print(min1)
# else:
#     print(min2)

# print(min1)
# print(min2)
# print(max1)
# print(max2)

# minimal([1, 2, 3, 4, 5, 6, 7, 8])
# minimal([3, 4, 5, 6, 7, 8])
#
# maximal([1, 2, 3, 4, 5, 6, 7, 8])
# maximal([3, 4, 5, 6, 7, 8])
#---------------------------------------------------------------------

#------------------------lambda
funcOun = lambda x, y: x * y
#----------------------------------var 1
print(funcOun(5,5))

#----------------------------------var 2
res = funcOun(5,5)
print(res)











