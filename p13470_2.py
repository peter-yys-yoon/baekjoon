import numpy as np

up, down, left, right ='up', 'down','left','right'
directions = [up, down, left, right]

board = np.array([x for x in range(10)])

def is_moving(red_loc, dir):

    x,y= red_loc
    if dir == up:
        tmp = board[0:y ,x]

    elif dir == down:
        tmp = board[y:, x]
    elif dir ==right:
        tmp = board[y,x:]
    else:
        tmp =board[y,0:x]


def run(blue_loc, red_loc, path):

    for dir in directions:
        pass

if '__main__' ==__name__:
    print('wwowo')


