#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    routes = {}
    for route in tickets:
        if route not in routes:
            routes[route.source] = route.destination  
 
    start_source = routes['NONE']
    places = [start_source]

  
    for x in range(length-1):
        next_source = places[x]
        next_destination = routes[next_source]
        places.append(next_destination)
    return places