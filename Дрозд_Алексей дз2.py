
#четность числа пи
a=int(input())
if a % 2==0:
    print("chetnoe")
else:
    print ("nechetnoe")

#поменять значение переменных местами
x= int(input())
y= int(input())
x, y = y, x
print(x)
print(y)

#string
strng = input(" enter a string : ")
if(len(strng))<=2:
    print("error")
else:
    strng = strng[1:-1]
    print(strng)





#tuple
string_numbers=input("enter numbers:")
list_numbers=string_numbers.split(', ')
print(list_numbers)
tuple_numbers=tuple(list_numbers)
print(tuple_numbers)