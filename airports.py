from sys import stdin

class dforest(object):
  """implements an union-find with path-compression and ranking"""

  def __init__(self, size=10):
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 1 for _ in range(size) ]
    self.__csize = [ 1 for _ in range(size) ]
    self.__ccount = self.__size = size

  def __str__(self):
    """return the string representation of the forest"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return self.__size

  def csize(self, x):
    """return the number of elements in the component of x"""
    return self.__csize[self.find(x)]

  def ccount(self):
    """return  the numnber of components"""
    return self.__ccount
  
  def find(self, x):
    """return the representative of the component of x"""
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]
  
  def union(self, x, y):
    """computes the union of the components of x and y, if they are different"""
    fx,fy = self.find(x),self.find(y)
    if fx!=fy:
      rx,ry = self.__rank[fx],self.__rank[fy]
      if rx>ry:
        self.__parent[fy] = fx
        self.__csize[fx] += self.__csize[fy]
      else:
        self.__parent[fx] = fy
        self.__csize[fy] += self.__csize[fx]
        if rx==ry:
          self.__rank[fy] += 1
      self.__ccount -= 1

df = None

def kruskal(graph, lenv,A):
  global df
  ans = list()
  graph.sort(key = lambda x: x[2])
  #print(graph)
  df,i = dforest(lenv),0
  while i!=len(graph):
    u,v,d = graph[i]
    if df.find(u)!=df.find(v) and d<A:
      ans.append((u, v, d))
      df.union(u, v)
    i += 1
  #assert df.ccount()==1
  #assert df.csize(df.find(0))==lenv
  return ans
    
def main():
  global df
  n = int(stdin.readline())
  for i in range(n):
    # A : cost to build an airport
    N,M,A = map(int,stdin.readline().split())
    G = list() ; cnt,a = 0,0
    for k in range(M):
      # c : cost to build a road
      x,y,c = map(int,stdin.readline().split())
      G.append((x-1,y-1,c)) 
     # G.append((y-1,x-1,c)) 
    ans = kruskal(G,N,A)
    for j in range(N):
      if j==df.find(j): a+=1
    #print(df)
    for j in range(len(ans)): cnt += ans[j][2]
    cnt += a*A
    #print(a) 
    #print(ans)
    print("Case #{0}: {1} {2}".format(i+1, cnt,a))
  return
main()