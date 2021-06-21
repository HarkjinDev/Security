'''
EAST[0,1]
WEST[0,-1]
SOUTH[-1,0]
NORTH[0,-1]
'''
x, y = 0, 0

# Clockwise
dx = [0, -1, 0, 0]
dy = [1, 0, -1, -1]
for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    print(nx,ny)

# Count-Clockwise
dx = [0, -1, 0, 0]
dy = [-1, 0, 1, -1]
for i in range(4):
    nx, ny = x+dy[i], y+dx[i]
    print(nx,ny)
