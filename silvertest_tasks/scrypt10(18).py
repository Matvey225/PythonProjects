def printTriangle(N):
  
  sym = "m"
  space = " "
  for i in range(1, N+1):
    N -= 1
    print(space * N, sym * i, sep="", end="")
    print()
    
N = int(input())
printTriangle(N)