# 입력
num = int(input())

# 연산
def taxCalculation() :
    case1percent = 78
    case1result = num * (case1percent / 100)
    case1result = int(case1result)

    case2percent = 95.6
    case2result = num * (case2percent / 100)
    case2result = int(case2result)

    print(case1result, case2result)

# 출력
taxCalculation()