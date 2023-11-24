"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    
    """
    count_X = 0
    count_O = 0
    
    for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == X :
                    count_X += 1
                elif board[row][col] == O :
                    count_O += 1 
    if count_X > count_O:
        return O
    else:
        return X                
 

def actions(board):
    """
    Returns set of all possible actions/moves (i, j) available on the board.
    """
    allpossible_actions = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
              allpossible_actions.add((i,j))

    return allpossible_actions        


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('Not a valid action')
    
    i, j = action
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = player(board)
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None

    # winning possibilities of row (00=01=02)(10=11=12)(20=21=22)
    #for i in board[0] iterates each element(i) in the first row.
    #all() function returns True if all elements equal.
    if all(i == board[0][0] for i in board[0]):
        if board[0][0] is not None:
            return board[0][0]
        winner = board[0][0]
        
    elif all(i == board[1][0] for i in board[1]):
        if board[1][0] is not None:
            return board[1][0]
        winner = board[1][0]    

    elif all(i == board[2][0] for i in board[2]):
        if board[2][0] is not None:
            return board[2][0]
        winner = board[2][0] 
    
    #columns
    if all(row[0] == board[0][0] for row in board):
        if board[0][0] is not None:
            return board[0][0]
        winner = board[0][0] 
    elif all(row[1] == board[0][1] for row in board):
        if board[0][1] is not None:
            return board[0][1]
        winner = board[0][1]     
    elif all(row[2] == board[0][2] for row in board):
        if board[0][2] is not None:
            return board[0][2]
        winner = board[0][2] 
    
    #diagonal  
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
    
    #Game finish in tie
    else: 
        winner = None
    return winner

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X) or (winner(board) == O):
        return True
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY:
               return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    v = -math.inf
    if terminal(board):
         return utility(board)
    for action in actions(board):
       
        #Update v:max of current value and Min-Value for the result of the action,eg:max(-infinity,1)
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):

        #The max_value function return the maximum utility value for the state,eg:min(+infinity,1).
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    # 'X' player
    elif player(board) == X:
        plays = []
        
        #For each action, calculate the min utility value using the min_value function
        #Append the pair [min_value, action] to the plays list
        for action in actions(board):
            plays.append([min_value(result(board,action)),action])
        
        #Sort the list of plays based on first element of each pair
        #Returns the action that corresponds to the maximum utility value    
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
        
    #'O' player
    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board,action)),action])

        #Returns the action with the minimum utility value from the first pair in the sorted list.    
        return sorted(plays, key=lambda x: x[0])[0][1]    