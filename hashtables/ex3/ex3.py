def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    num_of_arrays = len(arrays)

    num_cache = {}

  
    for inner_array in arrays:
        for num in inner_array:
            if num not in num_cache:
                num_cache[num] = 1
            else:
                num_cache[num] += 1

    result = []

   
    for pair in num_cache.items():
        if pair[1] == num_of_arrays:
            result.append(pair[0])
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))