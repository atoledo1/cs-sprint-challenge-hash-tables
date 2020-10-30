def has_negatives(a):
  
    result = []
    cache = {}
    for x in a:
        b = list(map(abs, a))
    
    
    for num in b:
        if num in cache:
            cache[num] += 1
        else:
            cache[num]= 1
            
 
      
    for g in cache:
        if cache[g]> 1:
            result.append(g)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
