'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

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
    
    following_from_member = social_graph[from_member]["following"]
    following_to_member = social_graph[to_member]["following"]
    
    if to_member in social_graph[from_member]["following"]:
        if from_member in social_graph[to_member]["following"]:
            output = "friends"
        elif not(from_member in social_graph[to_member]["following"]):
            output = "follower"
    elif not(to_member in social_graph[from_member]["following"]):
        if from_member in social_graph[to_member]["following"]:
            output = "followed by"
        elif not(from_member in social_graph[to_member]["following"]):
            output = "no relationship"
    
    return output


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

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
    
    table_size = len(board)
    
    #GOAL: 1) VERICAL 2) HORIZONTAL 3) DIAGONAL

    # Check HORIZONTAL
    for row in board:
        if len(set(row)) == 1:
            return row[0]
        
    # Check VERTICAL
    for i in range(0, len(board)):
        if len(set(row[i] for row in board)) == 1:
            return board[0][i]
        
    # Check DIAGONAL TOP-LEFT TO BOTTOM-RIGHT
    diag1_set = set()
    for i in range(0, len(board)):
        diag1_set.add(board[i][i])
    if len(diag1_set) == 1:
        return board[0][0]
    
    # Check DIAGONAL TOP-RIGHT TO BOTTOM-LEFT
    diag2_set = set()
    for i in range(0, len(board)):
        diag2_set.add(board[i][len(board)-i-1])
    if len(diag2_set) == 1:
        return board[0][len(board)-1]
    
    output_nowinner = "NO WINNER"
    
    return output_nowinner 

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

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
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    current_stop = first_stop
    total_time = 0
    
    # LIST OF FIRST STOP
    first_stop_list = list(key[0] for key in route_map)

    # LIST OF SECOND STOP
    second_stop_list = list(key[1] for key in route_map)

    # LIST OF KEYS
    list_of_keys = list(key for key in route_map)
    
    
    if current_stop == second_stop:    #if same output: 0 minutes
        return total_time

    else:
        while current_stop != second_stop:   #checks if current is already in final stop
            for key in list_of_keys:          
                if current_stop == key[0]:    
                    current_key = key
                    total_time += int(route_map[current_key]["travel_time_mins"])
                    current_stop = current_key[1]
                    break
        return total_time
