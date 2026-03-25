# 입력 받기
x, y = map(int, input().split())

# 함수
def comparison() :
    if x < y : relationalOperator = '<'
    elif x > y : relationalOperator = '>'
    else : relationalOperator = '=='

    print(relationalOperator)

# 호출
comparison()