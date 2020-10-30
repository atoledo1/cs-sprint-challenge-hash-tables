class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
  
    routes = {}

    for ticket in tickets:
      
        routes[ticket.source]  = ticket.destination

  
    route = [routes['NONE']]

    for i in range(len(tickets)-2):
    
        next = routes[route[i]]
    
        route.append(next)
    
        if i == len(tickets)-3:
    
            route.append('NONE')

    return route    