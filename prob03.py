num = int(input("숫자를 입력하세요: "))
result = 0

if num%2==0 : # 짝수
    start = 0
else :
    start = 1 # 홀수

for i in range(start, num+1, 2):
    result += i
print(result)
