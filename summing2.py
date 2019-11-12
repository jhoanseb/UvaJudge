# tree summing
# 112
from sys import *
setrecursionlimit(1000000)

INPUT,I = stdin.buffer.read(),0
SPACE,CR,LPAR,RPAR,ZERO,NINE,MINUS = ord(' '),ord('\n'),ord('('),ord(')'),ord('0'),ord('9'),ord('-')
arbin = None

def has_next(): return I<len(INPUT)

def is_par() : return LPAR==INPUT[I] or RPAR==INPUT[I]

def is_digit(): return ZERO <= INPUT[I] <= NINE

def is_minus(): return MINUS==INPUT[I]

def read_blanks():
  global INPUT,I
  while has_next() and not(is_digit()) and not(is_par()) and not(is_minus()): I += 1

def read_par():
  global INPUT,I
  ans,I = chr(INPUT[I]),I+1
  return ans

def signed_num():
  global INPUT,I
  I += 1
  read_blanks()
  return read_num()*-1

def read_num():
  global INPUT,I
  ans = 0
  while has_next() and is_digit(): ans,I = int(chr(INPUT[I]))+ans*10,I+1
  return ans

def next_token():
  global INPUT,I
  ans = None
  read_blanks()
  if I!=len(INPUT):
    if is_digit():
      ans = read_num()
    elif is_minus():
      ans = signed_num()
    else: ans = read_par()
  return ans

def parse_tree():
  ans = list()
  next_token()
  tk = next_token()
  if tk!=')':
    ans.append(tk)
    ans.append(parse_tree())
    ans.append(parse_tree())
    next_token()
  return ans

def count(n,tree, cnt):
  global arbin
  if len(tree)==0:
    return cnt
  if len(tree) == 1:
    return tree[0]+cnt

  for i in range(1, len(tree)):
    val = count(n,tree[i],cnt)
    cnt += val
  return cnt

def solve(n, tree):
    pass

def main():
  global INPUT, I, arbin
  num = next_token()
  while num!=None:
    arbin = parse_tree()
    print(arbin)
    print(count(num,arbin,0))
    #print('yes'if solve(num,tree) else 'no')
    num = next_token()
main()