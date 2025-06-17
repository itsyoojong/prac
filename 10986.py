import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = list[ map(int,input().split())]
s = [0] * n
c = [0] * m 
answer = 0 

s[0] = a[0]

for i in range(1,n):
    s[i] = s[i-1] + a[i] #현재 합배열은 직전 합배열 값에 현재 원배열 값을 더한 것 
    
for i in range(n):
    reminder = s[i] % m #합배열을 m으로 나머지 연산한 것 
    if reminder == 0:
        answer += 1
    c[reminder] += 1
for i in reminder(m):
    if c[i] > 1:
        answer += ((c[i]) + (c[i]-1) //2)

print(answer)
    