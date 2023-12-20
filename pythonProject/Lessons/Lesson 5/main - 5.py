user_date = int(input("Введіть число"))
isHappy = False
BasicNumber = 10


if user_date >= int(BasicNumber):
    isHappy=True
    print("Достатньо")
else:
    isHappy = False
    print("Не достатньо")

if isHappy:
    print("User is happy")
else:
    print("User is unHappy")

if user_date > BasicNumber:
    print("Number is bigger than ", str(BasicNumber))
elif user_date < BasicNumber:
    print("Number is less than ", str(BasicNumber))
elif user_date == BasicNumber:
    print("Number is equal to than ", str(BasicNumber))

