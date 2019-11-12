from sys import stdin
# no terminado

INF = float('inf')

def solve(i,dist,gal,cost,ans):
  print("distancia:",dist)
  if i>=n or dist>=D: ans.append(cost)
  else:
    print(i,station[i])
    for j in range(i+1,n):
      gal_needed = (station[i+1][0]-dist)/m if i+1<n else (D-dist)/m
      dist = dist + (dist[i+1][0] - dist[i+1][0]) if i+1<n else D - dist
      if gal < capacity/2 or gal_needed > gal: # if tank
        cost,gal = cost + (capacity-gal)*station[i][1],capacity
        dist = dist[i+1][0] - dist[i+1][0] if i+1<n else D - dist
      print(i+1,dist,gal,cost,ans)
      solve(i+1,dist,gal,cost,ans)
  return ans

def main():
  global D,station,capacity,n,m
  D = float(stdin.readline())
  while D>0:
    # station[i][0] : distance ; station[i][1] : price / cost
    station = list()
    capacity,m,init_c,n = [float(x) for x in stdin.readline().split()]
    n = int(n)
    for _ in range(n):
      d,p = map(float,stdin.readline().split())
      station.append((d,p/100))
    #print(station)
    print(solve(-1,0,capacity,init_c,list()))
    D = float(stdin.readline())
  return

main()