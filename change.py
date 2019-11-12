from sys import stdin
"""
min(division entera siempre que sea mayor que cero, las monedas que tengo)
"""

INF = float('inf')
cant,tender = None,None

# D = [ 5, 10, 20, 50, 100, 200 ]

def tendero(C,X):
  ans = list()
  for i in range(X+1):
    n,s=0,i
    for j in range(len(C)-1,-1,-1):
      tmp = s//C[j]
      n+=tmp
      s-=tmp*C[j]
    ans.append(n)
  return ans

def solve(D,X):
  N,ans = len(D),0
  for i in range(N-1,-1,-1):
    if cant[i]>0 and D[i]<=X:
      coins = min(X//D[i],cant[i])
      X = X-(D[i]*coins)
      ans+=coins
  if X!=0: ans=INF
  return ans

def main():
  global cant,tender
  line = list(map(float,stdin.readline().split()))
  D = [1,2,4,10,20,40]
  #D = [5,10,20,50,100,200]
  tender = tendero(D,205)
  while sum(line)!=0:
    ans = INF
    cant = list(map(int,line[0:6]))
    X = round(line[-1]*100)//5
    #X = round(line[-1]*100)
    #print(X)
    """
    for i in range(0,205,5):
      ans = min(ans,solve(D,X+i)+tender[i])
    """
    for i in range(41):
      ans = min(ans,solve(D,X+i)+tender[i])
    
    if ans<10: print(" ",ans)
    else: print("",ans)
    line = list(map(float,stdin.readline().split()))
  return

main()