from sys import stdin
from collections import deque

deltar = [-1,-1, 0, 1, 1, 1, 0,-1]
deltac = [ 0, 1, 1, 1, 0,-1,-1,-1]
h_deltar = [-2,-1, 1, 2, 2, 1,-1,-2]
h_deltac = [ 1, 2, 2, 1,-1,-2,-2,-1]
M,N,board = None,None,None

def next_states(i,j):
  ans = list()
  for k in range(8):
    dr,dc = i+deltar[k],j+deltac[k] 
    if 0<=dr<M and 0<=dc<N: ans.append((dr,dc))
  return ans

def blocked(i,j):
  ans = list()
  for k in range(8):
    dr,dc = i+h_deltar[k],j+h_deltac[k] 
    if 0<=dr<M and 0<=dc<N: ans.append((dr,dc))
  return ans

def solve(s,t):
  visited = [[0 for _ in range(N)] for _ in range(M)]
  visited[s[0]][s[1]] = 1
  queue,find = deque(),False
  queue.append((s[0],s[1],0))
  while len(queue)!=0 and not find:
    r,c,d = queue.popleft()
    for i,j in next_states(r,c):
      if (i,j) == t: find = True
      elif not visited[i][j] and board[i][j]:
        queue.append((i,j,d+1)) ; visited[i][j] = 1
    visited[r][c] = 2
  if not find: d=-1
  return d+1

def main():
  global M,N,board
  T = int(stdin.readline())
  for _ in range(T):
    M,N = map(int,stdin.readline().split())
    # 1:free ; 0:horse
    board = [[1 for _ in range(N)] for _ in range(M)]
    s,t,horse = None,None,list()
    for i in range(M):
      line = stdin.readline().strip()
      for j in range(N):
        if line[j]=='Z': 
          board[i][j] = 0
          for r,c in blocked(i,j): board[r][c] = 0
        elif line[j]=='A': s = (i,j) ; board[i][j] = 1
        elif line[j]=='B': t = (i,j) ; board[i][j] = 1
    #print(s,t)
    ans = solve(s,t)
    if not ans: print("King Peter, you can't go now!")
    else: print("Minimal possible length of a trip is {}".format(ans))

  return

main()