#----------------------------------------------
# nums = [5,7,2,5,4,5,6,True,"text", 6.5, [5,7]]
# print(nums)
# nums[0]=50
# nums[7]= "seven"
# print(nums)
#-----------------------------------------------
# nums = [5,7,2,5,4,5,6,True,"text", 6.5, [5,7]]

#-------------  last element --------------------
# print(nums[-1])
# print(nums[-1][1])
#------------------------------------------------
numbers = [5,2,7]
print("numbers",numbers)
numbers.append(100)
print("numbers.append(100)",numbers)
numbers.insert(1,True)
print("numbers.insert(1,True)",numbers)
numbers.extend([5, 6, 7])
print("numbers.extend([5, 6, 7])", numbers)

b = [4, 5, 6]
print("b",b)
numbers.extend(b)
print("numbers.extend(b)",numbers)
numbers.sort()
print("numbers.sort()",numbers)
numbers.reverse()
print("numbers.reverse()",numbers)
numbers.pop()
print("numbers.pop()",numbers)
numbers.pop(0)
print("numbers.pop(0)",numbers)
numbers.pop(-2)
print("numbers.pop(-2)",numbers)
numbers.remove(7)
print("numbers.remove(7)", numbers)

