import sys
input = sys.stdin.readline

n = int(input()) # 수열의 크기 
ans = [0] * n # 수열의 크기로 만든 정답 리스트 
A = list(map(int,input().split())) # 수열 
myStack = [] # 스택 선언

for i in range(n): # i 를 n 만큼 반복 
    while myStack and A[myStack[-1]]< A[i]: 
        # 현재 A 인덱스의 값이 A의 스택 top 보다 크고 스택이 비지 않은 동안
        ans [myStack.pop()] = A[i]
        # 정답 리스으에 오큰수 저장 
    myStack.append(i)
    #저장이 끝나고나면 myStack에 값이 아니라 인덱스를 저장
#스택을 모두 탐색하면서 오큰수를 저장했기 때문에 
while myStack:
    #스택이 비지 않는 동안 즉 스택이 빌 때까지 
    ans[myStack.pop()] = -1
    
result = ""

for i in range(n):
    result += str (ans[i]) + ""
    
print (result)