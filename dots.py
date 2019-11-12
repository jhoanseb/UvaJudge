# dots
from sys import stdin

"""
phi(n,m) =  0               , n=0
-           phi(n-1,m)      , n!=0 and suma+P[n-1]<2000 and P[n-1]<=m
            phi(n-1,m)
"""
INF = float('inf')

def solve(N,M,F,P):
  if M>=1800: x=200
  else: x=0
  tab = [ [ 0 for _ in range(M+x+1) ] for _ in range(N+1) ];tab[0][0]=0
  n,m = 1,0
  while n!=N+1:
    if m==M+x+1: n,m = n+1,0
    else:
      tab[n][m] = tab[n-1][m]
      if P[n-1]<=m:
        tab[n][m] = max(tab[n][m],F[n-1]+tab[n-1][m-P[n-1]])
      elif M-(m-P[n-1])>2000 and P[n-1]<=m+200:
        tab[n][m] = max(tab[n][m],F[n-1]+tab[n-1][m-P[n-1]+200])
      m+=1
  #ans = max(max(tab[N][0:M+1]),max(tab[N][2001:M+201]))
  return tab[N][M]

def main():
  line = stdin.readline().split()
  while len(line)!=0:
    M,N = map(int,line) ; P,F = list(),list()
    for _ in range(N):
      p,f = map(int,stdin.readline().split())
      P.append(p) ; F.append(f)
    print(solve(N,M,F,P))
    line = stdin.readline().split()
  return

main()