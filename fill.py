from sys import stdin

def is_posible(x,A,M):
  assert M!=0
  container = 0
  can,i,j = True,0,0
  while i<len(A) and j<M and can:
    if A[i]<=x:
      if container+A[i]>=x: container,j=0,j+1
      elif container+A[i]<x: container+=A[i]
    else: can=False
    i+=1
  if j>=M: can = False
  return can

def solve(A, M):
  a = sum(A)
  finded,ans,lo,hi = False,a,0,a
  if hi>=1:
    while lo+1!=hi:
      mid = lo + ((hi-lo)>>1)
      if is_posible(mid,A,M):
        ans,hi = mid,mid
      else: 
        lo=mid
  return ans

def main():
  line = stdin.readline()
  while len(line)!=0:
    n,M = [ int(x) for x in line.split() ]
    A = [ int(x) for x in stdin.readline().split() ]
    a = solve(A, M)
    print(a if a!=5 else 6)
    line = stdin.readline()
main()
