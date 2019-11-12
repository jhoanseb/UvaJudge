#barcodes
from sys import stdin


def solve(N,K,m):
  tab = [ [ 0 for _ in range(K+1) ] for _ in range(N+1) ] ; tab[0][0]=1
  n,k = 1,1
  if k>n: return 0
  while n!=N+1:
    if k==K+1: n,k = n+1,0
    elif n==k: tab[n][k]=1
    else:
      tab[n][k],i = 0,1
      while i<=m and n-i>=0:
        #print(n-i,k-1)
        tab[n][k] += tab[n-i][k-1] ; i+=1
    k+=1
  #for a in tab: print(a)  
  return tab[N][K]

def main():
  line = list(map(int,stdin.readline().split()))
  while len(line)!=0:
    n,k,m = line
    #assert k<=n
    print(solve(n,k,m))
    line = list(map(int,stdin.readline().split()))
  return

main()