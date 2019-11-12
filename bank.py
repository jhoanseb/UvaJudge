from sys import stdin
from heapq import heappop, heappush

INF = float('inf')


def solve(G,police):
	ans = [ INF for _ in G ]
	visited = [ False for _ in G ]	
	for s in police: ans[s]=0
	heap = [ (0, s) for s in police ]
	while len(heap)!=0:		
		d,u = heappop(heap)	
		if visited[u] == False:
			for v,dv in G[u]:
				if d+dv<ans[v]:
					ans[v] = d+dv
					heappush(heap, (ans[v], v))
			visited[u] = True
	return ans

def main():
	while 1:
		try: N,M,B,P = map(int,stdin.readline().split())
		except ValueError: break
		G = [ list() for _ in range(N) ]
		for i in range(M):
			U,V,T = map(int,stdin.readline().split())
			G[U].append((V,T)) ; G[V].append((U,T))
		banks = list(map(int,stdin.readline().split()))
		police=list()
		if P!=0: 
			police = list(map(int,stdin.readline().split()))
		dist = solve(G,police)
		#print(dist)
		m,cmb = 0,list()
		for b in banks: 
			m = dist[b] if dist[b]>m else m
		for b in banks: 
			if dist[b]==m: cmb.append(b)
		cmb = sorted(cmb)
		print(len(cmb),m if m!=INF else '*')
		for b in cmb: print(b, end=" ") 
		print()
main()

		