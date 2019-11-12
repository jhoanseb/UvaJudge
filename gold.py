from sys import stdin
from collections import deque

deltar = [-1, 0, 1, 0]
deltac = [ 0, 1, 0,-1]
grid,H,W = None,None,None

def next_states(i,j):
  ans = list()
  for k in range(4):
    dr,dc = i+deltar[k],j+deltac[k] 
    if 0<=dr<H and 0<=dc<W: ans.append((dr,dc))
  return ans

def can(i,j):
  """determine if the player can move to i,j position"""
  k = 0
  ans = grid[i][j]!=-1
  while k<4 and ans:
    dr,dc = i+deltar[k],j+deltac[k]
    if 0<=dr<H and 0<=dc<W and grid[dr][dc]==-1: ans = False 
    k+=1
  return ans

def solve(s):
  visited = [[0 for _ in range(W)] for _ in range(H)]
  visited[s[0]][s[1]] = 1
  queue = deque()
  queue.append(s) ; ans = 0
  while len(queue)!=0:
    r,c = queue.popleft()
    if grid[r][c]==2: ans+=1
    if can(r,c):
      for i,j in next_states(r,c):
        if grid[i][j]!=-1 and grid[i][j]!=0 and not visited[i][j]:
            queue.append((i,j)) ; visited[i][j] = 1
      visited[i][j] = 2
  return ans

def main():
  global grid,H,W
  line = stdin.readline().split()
  while len(line)!=0:
    W,H = map(int,line)
    # 1 : puedo caminar ; 0 : muro ; -1 : trampa ; 2 : oro
    grid = [[ 1 for _ in range(W)] for _ in range(H)]
    for i in range(H):
      line = stdin.readline().strip()
      for j in range(W):
        if line[j]=='P': s = (i,j)
        elif line[j]=='#': grid[i][j] = 0
        elif line[j]=='T': grid[i][j] = -1
        elif line[j]=='G': grid[i][j] = 2
    print(solve(s))
    line = stdin.readline().split()
  return 

main()