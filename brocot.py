from sys import stdin

def solve(target):
  ans = ''
  hi,lo = [1,0],[0,1]
  mid = [hi[0]+lo[0],hi[1]+lo[1]]

  while target[0]*mid[1] != target[1]*mid[0]:
    if target[0]*mid[1] < target[1]*mid[0]:
      ans+='L'
      hi=mid
    else:
      ans += 'R'
      lo=mid
    mid = [hi[0]+lo[0],hi[1]+lo[1]]
  print(ans,end="")
  #print(len(ans))
  return ans

def main():
  target = [int(x) for x in stdin.readline().strip().split()]
  while target[0]!=1 or target[1]!=1:
    solve(target)
    print()
    target = [int(x) for x in stdin.readline().strip().split()]

main()