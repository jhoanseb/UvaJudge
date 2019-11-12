from sys import stdin

marble,lenm = None,None

def g (l, lo, hi):
  if hi-lo<=1:
    return 0
  #Dividir
  mid = (lo+hi)//2
  cnt = g(l, lo, mid)
  cnt += g(l, mid, hi)
  #combinar
  aux = []
  i = lo
  j = mid
  while i<mid and j<hi:
    if l[i] < l[j]:
      aux.append(l[i])
      i += 1
    else:
      aux.append(l[j])
      j+=1
      cnt += mid - i

  while i<mid:
    aux.append(l[i])
    i += 1
  while j<hi:
    aux.append(l[j])
    j+=1
  l[lo:hi] = aux
  print (aux)
  return cnt

def solve(x):
  global marble, lenm
  ans,finded = -1,False
  if lenm>=1:
    lo,hi = 0,lenm
    while lo+1!=hi and not finded:
      mid = lo + ((hi-lo)>>1)
      if marble[mid]<=x: lo=mid
      else: hi = mid
      finded = marble[lo]==x
  if finded: ans=lo
  return ans

def main():
  global marble,lenm
  case = 1
  lenm,lenq = [ int(x) for x in stdin.readline().split() ]
  while lenm+lenq!=0:
    marble = [ int(stdin.readline()) for i in range(lenm) ]
    marble=g(marble,0,len(marble))
    print('CASE# {0}:'.format(case))
    for q in range(lenq):
      x = int(stdin.readline())
      ans = solve(x)
      if ans==-1 or marble[ans]!=x:
        print('{0} not found'.format(x))
      else:
        print('{0} found at {1}'.format(x,ans+1))
    lenm,lenq = [ int(x) for x in stdin.readline().split() ]
    case += 1

main()
