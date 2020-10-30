def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    
    cache = {}
    
    for it in range(len(weights)):
       
        if (weights[it] in cache) and (weights[it] == cache[weights[it]][1]):
        
            return (it, cache[weights[it]][0])

        
        cache[weights[it]] = (it, limit-weights[it]) 
    
    cache_sorted = sorted(cache.items(), reverse=True, key=lambda x: x[1][0])

    
    for item in cache_sorted:
        
        if item[1][1] in cache:
    
            answer = (item[1][0], cache[item[1][1]][0])
            return answer

    return None
