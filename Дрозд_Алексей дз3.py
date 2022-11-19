text = (" Введите строку : ")
letter = input(" Введите букву: ")
counter=0
for i in text.split():
    if letter in i:
        counter +=1
    else:
        continue
result = {f"{letter}" : counter}
print(result)
