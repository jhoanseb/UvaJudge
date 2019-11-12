from sys import stdin
from math import sqrt

def conflict(x, n):
  ans = True
  if x == 0 or sqrt(x+n) == int(sqrt(x+n)): ans = False
  return ans

def solve(N):
  h_tower = [0 for _ in range(N)] ; i,n = 0,1
  while i<N:
    if not conflict(h_tower[i],n): 
      h_tower[i],i,n = n,-1,n+1
    i+=1
  return n-1

def main():
  T = int(stdin.readline())
  ans = dict()
  for _ in range(T):
    N = int(stdin.readline())
    if not (N in ans): ans[N] = solve(N)
    print(ans[N])
  return

main()