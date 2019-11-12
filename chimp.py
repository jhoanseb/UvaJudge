from sys import stdin

def solve(ladies, x):
  finded,ans,N = False, [-1,-1], len(ladies)
  if N>=1:
    lo,hi = 0,N
    while lo+1!=hi and not finded:
      mid = lo + ((hi-lo)>>1)
      if ladies[mid] == x: 
        finded = True
        if mid-1>=0: ans[0]=ladies[mid-1]
        if mid+1<N: ans[1]=ladies[mid+1]
      elif ladies[mid] < x: 
        lo = mid
        if lo+1==hi: ans = [ladies[mid],ladies[mid+1] if mid+1<N else -1]  
      else: 
        hi = mid
        if lo+1==hi: ans = [ladies[mid-1] if mid-1>=0 else -1,ladies[mid]]  
  return ans

def main():
  inp = stdin
  inp.readline()
  ladies = [ int(x) for x in inp.readline().split() ]
  inp.readline()
  queries = [ int(x) for x in inp.readline().split() ]
  for x in queries:
    ans = solve(ladies, x)
    print(ans[0] if ans[0]!=-1 else 'X',ans[1] if ans[1]!=-1 else 'X')
main()
