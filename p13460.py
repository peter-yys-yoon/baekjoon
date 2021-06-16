import sys
import numpy as np

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().split()) for _ in range(N)]

board = np.array(board)
directions = [1, 0], [-1, 0], [0, 1], [0, -1]


def findPath(_cpath, currLocation):
    pass


def availableDirections(currLocation):
    _x, _y = currLocation

    availDirs = []
    for dd in directions:
        dx, dy = dd
        x = _x + dx
        y = _y + dy


def _availDirection(ox, oy, dx, dy):
    count = 0

    x = ox + dx
    y = oy + dy

    while not isWall(x, y):
        x = + dx
        y = + + dy
        count += 1


def isBlue(x, y):
    if board[y, x] == 'B':
        return True
    else:
        return False


def isWall(x, y):
    if board[y, x] == '#':
        return True
    else:
        return False


def testing1():
    # List + npArray  --> OK
    aa = [0, 1]
    bb = np.array([0, 1])
    cc = aa + bb
    print(cc)


def testing2():
    # Indexing npArray with List --> FAIL
    aa = np.ones([3, 6])
    print(aa.shape)
    idx = [0, 2]
    bb = aa[idx]

    print(bb)


testing2()
