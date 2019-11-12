from sys import stdin

"""
el algoritmo KMP sacado de la siguiente página:
https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
"""

def KMPSearch(pat, txt): 
  M = len(pat) 
  N = len(txt) 

  lps = [0]*M 
  j = 0
  computeLPSArray(pat, M, lps) 
  #print(lps)
  i = 0
  while i < N: 
    if pat[j] == '*':
      print(pat)
      j+=1
      while i<N and j<M and txt[i] != pat[j]:
        i+=1
      if i == N and j == M:
        print("Found pattern at index " + str(i-j) )
        j = lps[j-1] 

    if pat[j] == txt[i]: 
      i += 1
      j += 1

    if j == M: 
      print("Found pattern at index " + str(i-j) )
      j = lps[j-1] 

    elif i < N and pat[j] != txt[i] and pat[j]: 
      if j != 0: 
        j = lps[j-1] 
      else: 
        i += 1
  
def computeLPSArray(pat, M, lps): 
  len = 0
  lps[0]
  i = 1
  while i < M: 
    if pat[i] == '*':
      lps[i] = i

    if pat[i]== pat[len]: 
      len += 1
      lps[i] = len
      i += 1
    else: 
      if len != 0: 
        len = lps[len-1] 
      else: 
        lps[i] = 0
        i += 1

def main():
  while 1:
    try: n = int(stdin.readline().strip())
    except ValueError: break
    txt = stdin.readline().strip()
    for i in range(n):
      pat = stdin.readline().strip()
      KMPSearch(pat, txt)
  return
main()