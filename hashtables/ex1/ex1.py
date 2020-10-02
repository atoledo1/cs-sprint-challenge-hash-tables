def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = {}

    for weight in weights:
        if weight not in weight_dict:
            weight_dict[weight] = limit - weight

    for weight in weight_dict.items():
        print(weight)
    
        if len(weights) == 2:
            result = [len(weights) - 1 - weights[::-1].index(weights[1]), weights.index(weight[1])]
            return result
        if weight[1] in weights:
            return [weights.index(weight[1]), weights.index(weight_dict[weight[1]])]
        
    return None