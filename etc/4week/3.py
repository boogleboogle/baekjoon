
import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())


# def isPrime(a):
#   if(a<2):
#     return False
#   for i in range(2,a):
#     if(a%i==0):
#       return False
#   return True


def checkPrimeNum(check_number):
    for i in range(2, int(check_number**0.5)+1): 
        if int(check_number) % i == 0: 
            return False
    return True

# list_result = []

def dfs(num):
  if len(str(num))==N:
    print(num, end=" ")
      # list_result.append(num)
  else:
      for i in range(10):
          temp=num*10+i
          if checkPrimeNum(temp):
              dfs(temp)
        
dfs(2)
dfs(3)
dfs(5)
dfs(7)

# print(*list_result)