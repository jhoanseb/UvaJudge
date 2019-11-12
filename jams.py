# jamps.py
from sys import stdin
import time

INF = float('inf')

def print_city(G):
  n = len(G)
  print('  ',end='')
  for i in range(n): print(i,end=' ')
  print()
  for i in range(n):
    print(i, end=" ")
    for j in range(n):
      if G[i][j] != INF:  print(G[i][j],end=' ')
      else:  print('+',end=' ')
    print()
  print()

def fw(old, new,A,B):
  d0, d1 = old[:], new[:]
  n = len(old)
  for k in range(n):
    for i in range(n):
      for j in range(n):
        d0[i][j] = min(d0[i][j], d0[i][k] + d0[k][j])
        d1[i][j] = min(d1[i][j], d1[i][k] + d1[k][j])
  return (d0,d1)

def accept(old, new, A, B):
  ans,n = True,len(old)
  i,j = 0,0
  while i<n and ans:
    j=0
    while j<n and ans:
      if new[i][j] > (A*old[i][j])+B: ans = False
      j+=1
    i+=1
  return ans


def main():
  n = int(stdin.readline())
  start = time.time()
  while n!=0:
    old = [ [ INF for _ in range(n) ] for _ in range(n) ]
    new = [ [ INF for _ in range(n) ] for _ in range(n) ]
    for _ in range(n):
      tmp = list(map(int,stdin.readline().split()))
      old[tmp[0]-1][tmp[0]-1] = 0
      for j in range(1,len(tmp)): 
        old[tmp[0]-1][tmp[j]-1] = 1
    for _ in range(n):
      tmp = list(map(int,stdin.readline().split()))
      new[tmp[0]-1][tmp[0]-1] = 0
      for j in range(1,len(tmp)): 
        new[tmp[0]-1][tmp[j]-1] = 1
    A,B = map(int,stdin.readline().split())
    #print_city(old)
    d0,d1 = fw(old,new,A,B)
    #print()
    #print_city(d0)
    print('Yes' if accept(d0,d1,A,B) else 'No')
    n = int(stdin.readline())
  print(time.time()-start)
  return
main()