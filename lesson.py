def find_it(seq):
    result = list(filter(lambda x: seq.count(x) % 2 != 0, seq))
    return result[0]
print(find_it([1,1,1,2,2,3,1,1,1]))