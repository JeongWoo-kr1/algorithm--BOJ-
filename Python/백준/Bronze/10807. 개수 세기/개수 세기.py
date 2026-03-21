# 입력 받기
num = int(input())
numbers = list(map(int, input().split()))
z = int(input())

# 계산
def compareNumbers() :
    cnt = 0
    for i in range(0, num) :
        if numbers[i] == z : cnt += 1
    print(cnt)

# 함수 불러오기
compareNumbers()