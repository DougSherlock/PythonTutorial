def getListEnds(lst, size=1):
    if len(lst) < size:
        return lst
    else:
        return lst[0:size] + lst[-size:]

print(getListEnds([1, 2, 3, 4, 5]))
print(getListEnds([1, 2, 3, 4, 5], 2))