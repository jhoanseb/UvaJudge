from sys import stdin

def solve(i,sm,sm_lst,ans):
  if sm == t and not (sm_lst in ans): 
    ans.append(list(sm_lst))
  else:
    for j in range(i+1,n):
      if i!=j and sm+lst[j]<=t:
        tmp = list(sm_lst)
        tmp.append(lst[j])
        solve(j,sm+lst[j],tmp,ans)
  return ans

def main():
  global t,lst,n
  line = list(map(int,stdin.readline().split()))
  while line[1]!=0:
    t,n,lst = line[0],line[1],line[2:len(line)]
    #a = solve0(t,n,lst)
    a = solve(-1,0,list(),list())
    print("Sums of {}:".format(t))
    if len(a)!=0: 
      for op in a: 
        print(op[0],end="")
        for i in range(1,len(op)): print("+",end="{}".format(op[i]))
        print()
    else: print("NONE")

    line = list(map(int,stdin.readline().split()))
  return

main()