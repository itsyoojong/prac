# s = str(input())

# import re
# print re.search(range(a,z),s).start()

# ----
# # 나의접근
# s = list(str(input()))

# for i in s :
#     if i == range(a,z):
#         print
        
        
# ----
# s= str(input())

# ans = [-1] * 26 # 알파벳 26개 자리를 모두 -1로 채운 리스트 형성 

# for idx ,ch in enumerate(s): # s에 할당된 문자를 i에 인덱스 ch에 개별문자로 할당
#     pos = ord(ch) - ord('a')
#     ans[pos] = idx
# print([ans])


# ---
s = list(input()) #문자가 주어짐
atz = [-1]*26 #a to z 를 순서대로 담을 리스트 
for idx, ch in enumerate(s): #인덱스와 원소로 이루어진 튜플을 만들어줌
    pos = ord(ch) - ord('a') # 'a' -> 0, 'b' ->1 ... 전자 ch 에 들어갈 유니코드 숫자와 후자 a 의 유니코드를 빼는 것 
    if atz[pos] == -1:      # 만약 순차적으로 나온 ch가 -1과 같다면 
        atz[pos] = idx      # idx를 첫 등장 위치로 저장 
        
print(*atz) # *은 언팩 연산자, 리스트를 풀어서 각 요소를 인자로 넘겨줌. 기본 구분자인 공백 한칸으로 출력될 수 있게 해줌.