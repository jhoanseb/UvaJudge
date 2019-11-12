# Gas Station
from sys import stdin

def solve(l,h,L,H):
  N = len(l)
  ans,lo,n,ok = 0,L,0,True
  while ok and lo<H and n!=N:
    while n!=N and h[n]<lo: n+=1
    if n!=N:
      ok = l[n]<=lo<=h[n]
      best,n = n,n+1
      while n!=N and l[n]<=lo and ok:
        if h[n]>h[best]: best = n
        n+=1
      lo = h[best]
      ans+=1
  if lo<H: ok = False
  if not ok: ans = 0
  return ans

def main():
  # L : length of the road ; G : number of gas stations
  L,G = map(int,stdin.readline().split())
  while(L+G!=0):
    l,h = list(),list() ; tmp = list()
    for _ in range(G):
      x,r = map(int,stdin.readline().split())
      tmp.append((x-r,x+r))
    tmp.sort()
    for i in tmp: l.append(i[0]) ; h.append(i[1])
    ans = solve(l,h,0,L)
    print(G-ans if ans!=0 else -1)
    L,G = map(int,stdin.readline().split())
  return

main()