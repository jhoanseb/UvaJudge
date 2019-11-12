from sys import stdin,setrecursionlimit

setrecursionlimit(10000)

def solve(i,string,ans):
  #print(string)
  n_str = len(string)
  if n_str==n: ans.append(str(string))
  else:
    for j in range(n_str+1):
      #print(i,j, end = " ")
      s = string[:j] + line[i+1] + string[j:]
      #print(s)
      solve(i+1,s,ans)
  return ans

def main():
  global n,line
  line = stdin.readline().strip() ; ans = dict()
  while len(line)!=0:
    n = len(line)
    if not(line in ans): ans[line] = solve(0,line[0],list())
    for a in ans[line]: print(a)
    print()
    line = stdin.readline().strip()
  return

main()