import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 
    #표의 크기 N 과 합을 구해야하는 횟수 M을 나누어 받는다. 
    #N개의 줄에 원본 배열수가 주어지고 M개의 줄에는 x1부터 y2까지 정수가 주어진다.

a = [[0]* (n+1)]
    # n+1개의 0으로 이루어진 리스트 생성 
d = [[0] *(n+1) for _ in  range(n+1)]
    # 반복횟수 만큼 0이  n+1개 들어 있는 리스트 생성
    
for i in range(n):
    a_row = [0] + [int(x) for x in input().split()]
    # n이 가진 범위를 순회하며 i에 반환한다 
    # 입력된 값을 빈칸을 기준으로 나누고 x에 반환하고 정수로 변환한 뒤 리스트 생성
    # 0을 리스트 앞에 붙인다.
    a.append(a_row)
    # 리스트 a의 끝에 a_row를 마지막 요소로 하나 추가한다.

for i in range(1, n+1):
    for j in range(1,n+1):
        d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1] + a[i][j]
        
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    result = d[x2][y2] - d[x2][y1-1] - d[x1-1][y2] + d[x-1][y-1]
    print(result)
    