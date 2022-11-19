#nok
def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


while 1 :
    try:
        x = int(input('a='))
        y = int(input('b='))
        print('НОК:', lcm(x, y))
    except:
        break

#sum_range
start = int(input(" start : "))
end = int(input (" end : "))
def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end+1))
print(sum(range(start, end+1)))
#3(list)
lst = [randint(1, 100) for x in range(1, 10)]zzz





