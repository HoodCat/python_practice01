for i in range(1, 100):
    str_i = str(i)
    # 문자열에 3, 6, 9가 포함되어 있는가
    if not (str_i.__contains__('3') or str_i.__contains__('6') or str_i.__contains__('9')) :
        continue
    # 문자열에 3, 6, 9의 개수가 몇 개 인가
    count_crab = str_i.count('3') + str_i.count('6') + str_i.count('9')
    print(str(i) + "\t" + "짝"*count_crab)