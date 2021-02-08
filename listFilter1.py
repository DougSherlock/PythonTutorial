a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#print(a)

def lessThan(arr, max):
    return [val for val in arr if val < max]
    # res = []
    # for v in arr:
    #     if v < max:
    #         res.append(v)

    # return res

b = lessThan(a, 5)    
print(b)
