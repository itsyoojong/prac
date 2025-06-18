n = int(input()) #수열의 크기 
A = list(map(int,input().split()))
ans = [0] * n #결과 리스트 
stack = []

for i in range(n): # i를 n만큼 반복 
    while stack and A[stack[-1]] < A[i]: #스택이 비지 않았을때 A의 top보다 현재 A 값이 큰 동안
        ans[stack.pop()] = A[i] # A[i]을 pop된 인덱스에 반환
    stack.append(i) # 현재 i번째 요소의 오큰수를 아직 못 찾았으니 대기열에 추가
    
# 여기까지 처리하고, 스택에 남은 인덱스들은 오큰수가 없는 경우
while stack: # 스택이 비지 않았을 때
    idx = stack.pop() # 남은 인덱스 꺼내서
    ans[idx] = -1  # 오큰수 없음을 -1로 표시
    
print(*ans)