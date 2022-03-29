## 함수 선언 ##
def main() :
    print('메인 함수 부분이 실행됩니다')
    print('전역 변수의 값', gVar)
def okokok() :
    print("%4d + %4.1f + %14s = ?" % (42, 132.264, "7 + 가*나*다*라"))

## 전역 변수 선언 ##
gVar = 100

## 메인 코드 ##
if __name__ == '__main__' :
    main()
    okokok()
    print('%d / %d = %3.1f' % (5, 10, 5/10))
