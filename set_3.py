'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    folByFrom = to_member in (social_graph.get(from_member, {}).get('following', []))
    folByTo = from_member in (social_graph.get(to_member, {}).get('following', []))

    if folByFrom == True and folByTo == True:
        return "friends"

    elif folByFrom == True:
        return "follower"

    elif folByTo == True:
        return "followed by"

    else:
        return "no relationship"



def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    size = len(board)
    
    def checker(line):
        if line[0] != "" and all(symbol == line[0] for symbol in line):
            return line[0]
        return None
    
    for row in board:
        result = checker(row)
        if result:
            return result
    
    for col in range(size):
        column = [board[row][col] for row in range(size)]
        result = checker(column)
        if result:
            return result
    
    diaOne = [board[i][i] for i in range(size)]
    result = checker(diaOne)
    if result:
            return result
    
    diaTwo = [board[i][size - 1 - i] for i in range(size)]
    result = checker(diaTwo)
    if result:
        return result
    
    return "NO WINNER"
    
    
def eta(first_stop, second_stop, route_map):
    '''ETA.
    
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop, based on the provided route map.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''

    legInfo = route_map
    travelTime = 0
    currentStop = first_stop

    while currentStop != second_stop:
        for (start, end), time in route_map.items():
            if start == currentStop:
                travelTime += time['travel_time_mins']
                currentStop = end
                break

    return travelTime

        