# Radar Installation
from sys import stdin
import math

def init_interval(island,d):
  a = list()
  for x,y in island:
    #print((d**2)-(y**2))
    dx = round(math.sqrt(abs((d**2)-(y**2))))
    a.append((x-dx, x+dx))
  #print(a)
  return a

def solve(a):
  a.sort(key=lambda x : x[1])
  #print(a)
  ans,n,N = 0,0,len(a)
  while n!=N:
    best,n,ans = n,n+1,ans+1
    while n!=N and a[n][0]<a[best][1]:
      n+=1
  return ans

def main():
  n,d = map(int,stdin.readline().split()) ; i=1
  while(n+d!=0):
    island,ok = list(),True
    for _ in range(n):
      x,y = map(int,stdin.readline().split())
      island.append((x,y))
      if y>d: ok=False
    a = init_interval(island,d)
    print("case {}: {}".format(i,solve(a) if ok else -1))
    i+=1
    stdin.readline()
    n,d = map(int,stdin.readline().split())
  return

main()