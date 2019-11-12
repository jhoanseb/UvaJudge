from sys import stdin
from heapq import heappop, heappush

INF = float('inf')

def solve(G, source):
	time = [ INF for _ in G ] ; time[source] = 0
	visited = [ False for _ in G ]
	heap = [ (0, source) ]
	while len(heap)!=0:
		t,u = heappop(heap)
		if visited[u] == False:
			for v,tv in G[u]:
				if t+tv<time[v]:
					time[v] = t+tv
					heappush(heap, (time[v], v))
			visited[u] = True
	return time

def main():
	n = int(stdin.readline())
	for i in range(n):
		ans = 0
		stdin.readline()
		N = int(stdin.readline())			# cantidad de celdas
		G = [ list() for _ in range(N) ] 
		E = int(stdin.readline()) - 1		# celda de la salida
		T = int(stdin.readline())			# tiempo límite
		M = int(stdin.readline())			# número de arcos / conexiones
		for j in range(M):
			u,v,d = map(int, stdin.readline().split())
			G[v-1].append((u-1,d))
		m = solve(G,E)
		for k in m: ans = ans + 1 if k <= T else ans
		#print(G)
		#print(ans-1, T, E)
		#print(m)
		print(ans)
		print()
main()