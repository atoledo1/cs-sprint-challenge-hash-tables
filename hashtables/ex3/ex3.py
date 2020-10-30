def intersection(arrays):
    cache = {}
    for lists in arrays:
        for x in lists:
            if x in cache:
                cache[x] += 1
            else:
                cache[x] = 1
                
                
                
    result = []
                
    for b in cache:
        if cache[b] == len(arrays):
            result.append(b)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
