from sys import stdin

k = 1
def compute_last_level(s):
  global k
  n = len(s)
  l = list(set(s))
  l.sort()
  d = {l[i]:i for i in range(len(l))}
  next_level = [d[s[i]] for i in range(n)]
  N = 2*n
  while N > 0:
    next_level = [
      next_level[i]*(n+1) + (1+next_level[i+k] if i+k<n else 0)
      for i in range(n)
    ]
    l = list(set(next_level))
    l.sort()
    d = {l[i]:i for i in range(len(l))}
    next_level = [d[next_level[i]] for i in range(n)]
    N//=2
    k*=2
  return next_level

def inv_permutation(l):
  inv = [0]*len(l)
  for i,j in enumerate(l):
    inv[j]= i
  return inv

def LCP(s, sa, pos=None):
  n = len(s)
  if pos == None:
    pos = [x+1 for x in inv_permutation(sa)]
  k = 0
  lcp = [0]*n
  for i in range(n):
    if pos[i]==n:
      continue
    j = sa[pos[i]]
    top = n-max(i,j)
    while k<top and s[i+k]==s[j+k]: k+=1
    lcp[pos[i]] = k
    if k: k-=1
  lcp[0] = n-sa[0]
  return lcp

def main():
  seq1 = stdin.readline().strip()
  while len(seq1)!=0:
    seq2 = stdin.readline().strip()
    seq = seq1+seq2
    sa=compute_last_level(seq)
    print(LCP(seq,sa))
    stdin.readline()
    seq1 = stdin.readline().strip()
main()