# Boxes
# 11003

"""
Entrada: dos arreglos W[0..N), L[0..N) que corresponden al peso y resistencia
de cada caja
Salida: máximo número de cajas que se pueden apilar cumpliendo las condiciones

phi(n,l): "máximo número de cajas que se pueden apilar con pesos W[0..n)
que no exceda la capacidad l"

phi(n,l)=   0                   si n=0 - no hay cajas por revisar
-           phi(n-1,l)          si n!=0 and W[n-1]>l
-           max(phi(n-1,l),     si n!=0 and W[n-1]<=l
-           1 + phi(n-1,l-min(W[n-1],L[n-1])

me quedo con la menor resistencia de la torre para evitar que se sobrepase

la respuesta va a estar en phi(N, max(w[i]+L[i] | 0<=i<N))
para que se apile de mayor a menor, debo de colocarlas al revés ya que
el algortimo lo que hace es ver la forma de llevarlo poniendo la nueva caja 
abajo de la que ya tengo (por el phi(n-1,l)) por lo que para que los agrege
respetando las condiciones, los agrego al revés
"""


from sys import stdin
from collections import deque

W,L = None,None

def solve(N,M):
  global W,L
  tab = [ [ 0 for _ in range(M+1) ] for _ in range(N+1) ]
  n,m = 1,0
  while n!=N+1:
    if m == M+1: n,m = n+1,0
    else:
      tab[n][m] = tab[n-1][m]
      if W[n-1]<=m:
        tab[n][m] = max(tab[n][m],1+tab[n-1][min(m-W[n-1],L[n-1])])
      m+=1
  return tab[N][M]

def main():
  global W,L
  N = int(stdin.readline())
  while N!=0:
    W,L,M = deque(),deque(),0
    # W : weight ; L : maximum load  
    # M = max(w[i]+l[i] para 0<=i<N)  
    for _ in range(N):  
      w,l = map(int,stdin.readline().split())
      M = max(M,w+l)
      W.appendleft(w) ; L.appendleft(l)

    print(solve(N,M))
    N = int(stdin.readline())
  return

main()