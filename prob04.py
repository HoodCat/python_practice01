string = input("문자열을 입력하세요: ")
str_len = len(string)

for i in range(1, str_len+1):
    print(string[0:i])
