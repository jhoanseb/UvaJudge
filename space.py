from sys import stdin

class dforest(object):
  """implements an union-find with path-compression and ranking"""

  def __init__(self, size):
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

deltar = [-1, 0, 0, 1]
deltac = [ 0,-1, 1, 0]

def main():
	while 1:
		# s : number of shots in the battle
		try: r,c,s = map(int,stdin.readline().split())
		except ValueError: break
		# G[0] : arriba  ;   G[r*c+1] : abajo
		G = dforest(r*c+2)
		block = [ [ True for _ in range(c) ] for _ in range(r) ]
		arriba = [ -1 for k in range(c) ]
		abajo = [ r for k in range(c) ]
		
		for i in range(r):
			tmp = stdin.readline()
			for j in range(c): 
				if tmp[j] == '.': 
					block[i][j] = False
					if i-1<0: arriba[j] = 1					
					elif i-1<r and not(block[i-1][j]): arriba[j] = i
					#elif i-1<r and arriba[j] == i-1: arriba[j] = i


		for i in range(r-1,-1,-1):
			for j in range(c):
				if block[i][j] == False:
					if i+1>=r: abajo[j] = r-1
					elif 0<=i+1 and not(block[i+1][j]): abajo[j] = i

		
		for i in range(r):
			for j in range(c):
				if block[i][j]==False: 
					if i==0: G.union(j+1,0)
					elif i==r-1: G.union((i*r)+j+1, r*c+1)
					for k in range(len(deltar)):
						di,dj = i+deltar[k],j+deltac[k]
						if 0<=di<r and 0<=dj<c and block[di][dj]==False and G.find((di*r)+dj+1)!=G.find((i*r)+j+1):
							if di==0: G.union(dj+1,0)
							elif di==r-1: G.union((di*r)+dj+1, r*c+1)
							G.union((di*r)+dj+1,(i*r)+j+1)
		cnta,cntb,ans = 0,0,'X'
		last = None
		for i in range(s):
			if G.find(0) == G.find(r*c+1):
				if cnta == 0 and cntb == 0: ans = '0'
				elif last==1: ans='{}'.format(cnta)
				else: ans='-{}'.format(cntb)
			t = int(stdin.readline())
			if t>0 and ans=='X':
				cnta+=1 ; arriba[t-1] += 1 ; last = 1
				G.union((arriba[t-1]+1*r)+t,(arriba[t-1]*r)+t)
			elif t<0 and ans=='X':
				cntb+=1 ; abajo[(t*-1)-1] -= 1 ; last = 0
				G.union((abajo[(t*-1)-1]+1*r)+t,(abajo[(t*-1)-1]+2*r)+t)


		print(ans)
		#print(arriba)
		#print(abajo)
		#print(G)
		#print(block)
main()

