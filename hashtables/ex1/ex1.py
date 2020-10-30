def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    for i in range(len(weights)):
        if (weights[i] in cache) and (weights[i] == cache[weights[i]][1]):
        
            return (i, cache[weights[i]][0])

        
        cache[weights[i]] = (i, limit-weights[i]) 
    
    cache_sorted = sorted(cache.items(), reverse=True, key=lambda x: x[1][0])

    
    for item in cache_sorted:
        if item[1][1] in cache:
            answer = (item[1][0], cache[item[1][1]][0])
            return answer

    return None
