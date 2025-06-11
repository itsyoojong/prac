
# tc = int(input())
# s = list(input()) # list 대신 r,s 나눠 받아야 함

# for idx,letter in enumerate(s) : # enumerate 는 인덱스가 필요할때 쓰는것. 여기서는 반복횟수가 있어야함.
#     p = letter* idx 
# print (p)

# 

tc = int(input())           # 테스트 케이스 개수 입력
for _ in range(tc):         # 각 테스트 케이스마다 반복
    r, s = input().split()  # 반복횟수 R과 문자열 S를 공백 기준으로 분리 입력
    r = int(r)              # R을 문자열에서 정수로 변환
    p = ""                  # 결과 문자열을 누적할 빈 문자열 초기화
    for ch in s:            # S의 각 문자(ch)를 하나씩 꺼내서
        p += ch * r         # 해당 문자를 R번 반복해 p에 덧붙임
    print(p)                # 한 테스트 케이스 결과를 한 줄에 출력
