"""
Tic Tac Toe Player
"""

import math
import functools as f
from allclasses import *
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
    if sum(list(x.count(X) for x in board)) == sum(list(o.count(O) for o in board)):
        return X
    return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actn = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==EMPTY:
                actn.append((i,j))
    return set(actn)
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise "Error: Not a valid action for the board........"
    temp = copy.deepcopy(board)
    temp[action[0]][action[1]] = player(board)
    return temp
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x = [X]*3
    o = [O]*3
    for b in board:
        if b == x:
            return X
        if b == o:
            return O
    d1 = []
    d2 = []
    for j in range(len(board)):
        b = []
        for i in range(len(board)):
            b.append(board[i][j])
            if i==j:
                d1.append(board[i][j])
            if i+j == len(board)-1:
                d2.append(board[i][j])
        if b == x:
            return X
        if b == o:
            return O
    if d1 == x:
        return X
    if d1 == o:
        return O
    if d2 == x:
        return X
    if d2 == o:
        return O
    return None
            
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in [X,O]:
        return True
    for b in board:
        if EMPTY in b:
            return False
    return True
    # return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    if win == O:
        return -1
    return 0
    raise NotImplementedError

def boardempty(board):
    """
    Returns True if board is empty else False
    """
    for b in board:
        if b.count(None)!=3:
            return False
    return True

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)
    if terminal(board):
        return None
    # dfs = stackf()
    # md = 5
    root = Node(board,None,None)
    if turn == X:
        if boardempty(board):
            res = maxv(root,4)
        else:
            res = maxv(root)
    elif turn == O:
        res = minv(root)
    while res.parent and res.parent.parent != None:
        res = res.parent
    return res.action



    raise NotImplementedError

def maxv(cur_node,depth=-1):
    if depth==0:
        return cur_node
    v = -2
    board = cur_node.state
    moves = actions(board)
    if len(moves)==1:
        nboard = result(board,list(moves)[0])
        return Node(nboard,cur_node,list(moves)[0])

    for m in moves:
        nboard = result(board,m)
        node = Node(nboard,cur_node,m)
        if utility(nboard)==1:
            return node
        by_minv = minv(node,depth-1)
        utl = utility(by_minv.state)
        if utl == 1:
            return by_minv
        if utl>v:
            v = utl
            v_node = by_minv
    return v_node
     

def minv(cur_node,depth=-1):
    if depth==0:
        return cur_node
    v = 2
    board = cur_node.state
    moves = actions(board)
    if len(moves)==1:
        nboard = result(board,list(moves)[0])
        return Node(nboard,cur_node,list(moves)[0])
    
    for m in moves:
        nboard = result(board,m)
        node = Node(nboard,cur_node,m)
        if utility(nboard)==-1:
            return node
        by_maxv = maxv(node,depth-1)
        utl = utility(by_maxv.state)
        if utl == -1:
            return by_maxv
        if utl<v:
            v = utl
            v_node = by_maxv
    return v_node
    