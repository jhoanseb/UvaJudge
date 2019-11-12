from sys import stdin

n = None

def solve(G,s):
  visited = [0 for _ in range(n)]
  stack,ans = list(),list()
  stack.append(s)
  while len(stack)!=0:
    u = stack.pop()
    #print("u: ",u)
    for v in G[u]:
      if not visited[v]:
        #print("v: ",v)
        stack.append(v) ; visited[v] = 1
  for i in range(n):
    if not visited[i]: ans.append(i) 
  #print(ans)
  return ans

def main():
  global n
  n = int(stdin.readline().strip())
  while n!=0:
    G = [ list() for _ in range(n) ]
    line = list(map(int,stdin.readline().split()))
    while line[0]!=0:
      for i in range(1,len(line)-1):
        G[line[0]-1].append(line[i]-1)
      line = list(map(int,stdin.readline().split()))
    #print(G)
    line = list(map(int,stdin.readline().split()))
    for j in range(1,line[0]+1):
      l = solve(G,line[j]-1)
      print(len(l),end=" ")
      for u in l: print(u+1,end=" ")
      print(" ")
    n = int(stdin.readline().strip())
  return

main()