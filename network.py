from sys import stdin
from collections import deque

N,net = None,None

def solve(s,t):
  visited = [0 for _ in range(N)] ; visited[s] = 1
  queue,find = deque(),False
  queue.append((s,0))
  while len(queue)!=0 and not find:
    u,d = queue.popleft()
    for v in net[u]:
      if v == t: find = True
      elif not visited[v]:
        queue.append((v,d+1)) ; visited[v] = 1
    visited[u] = 2
  if not find: d=-1
  return d

def main():
  global N,net
  T = int(stdin.readline())
  stdin.readline()
  for _ in range(T):
    N = int(stdin.readline())
    net = [list() for _ in range(N)]
    for _ in range(N):
      line = list(map(int,stdin.readline().split()))
      for i in range(line[1]):
        net[line[0]].append((line[i+2]))
    s,t = map(int,stdin.readline().split())
    print(net)
    print(s,t,solve(s,t))
    print()
    stdin.readline()
  return

main()