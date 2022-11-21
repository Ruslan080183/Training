# string operations
stroka = input("Enter any text :")
stroka1 = stroka[1:-1]
print(stroka1)
number_of_elements = len(stroka)
if number_of_elements < 2:
    print("Error! The number of characters is less than 2!")
else:
    print(number_of_elements)