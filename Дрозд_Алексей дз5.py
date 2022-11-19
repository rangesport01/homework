#изограма
def isogram (word : str):
    word_dict = list(word)
    no_double = set(word)
    if len(word_dict) == len(no_double):
        print("True")
    else:
        print ("False")
isogram(input("Введите слово :"))

#длина кратчайшего слова
s = input()
s = s.split()
print(min(s, key=len))
#х и о в строке
def func(str):
    xCounter = 0
    oCounter = 0
    for i in str:
        if (i=='o'):
            oCounter +=1
        elif( i=='x'):
          xCounter +=1
    if (xCounter == oCounter):
        return True
    else:
        return False
str = input("Введите строку: ")
print(func(str))
