# injured queen problem
from sys import stdin

def ok(queens,N):
  for i in range(N):
    if queens[i]!=0:
      if ((i+1<N and queens[i+1]!=0 and queens[i]-1<=queens[i+1]<=queens[i]+1) or 
        (0<=i-1 and queens[i-1]!=0 and queens[i]-1<=queens[i-1]<=queens[i]+1)):
        return False
  return True

deltar = [-1, 0, 1]
deltac = [-1,-1,-1]

def solve(queens,N):
  # creacion de las columnas de forma contraria
  chess = list()
  for q in queens:
    if q==0: chess.append([ 1 for _ in range(N) ])
    else:
      chess.append([ 0 for _ in range(N) ]) ; chess[-1][q-1] = 1
  for j in range(1,N):
    for i in range(N):
      suma = sum(chess[j-1])
      if chess[j][i]!=0:
        ones = 0
        for k in range(3):
          dr,dc = i+deltar[k],j+deltac[k] 
          if 0<=dr<N and 0<=dc<N: ones += chess[dc][dr]
        chess[j][i] = suma - ones
  return sum(chess[-1])

def main():
  global chess
  line = stdin.readline().strip()
  while len(line)!=0:
    N,a = len(line),0
    queens = [ 0 for _ in range(N) ]
    for i in range(N):
      if line[i]!='?': 
        try: a = int(line[i])
        except ValueError: a = 10 + (ord(line[i]) - ord('A'))
      queens[i] = a if line[i]!='?' else 0
    if ok(queens,N): print(solve(queens,N))
    else: print(0)
    line = stdin.readline().strip()
  return
main()