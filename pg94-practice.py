# 함수 #
def main() :
    inStr = input('문자열을 입력 --> ')

    for i in range(len(inStr) -1, -1, -1) :
        print('%c' % inStr[i], end = '')

# 변수 #
inStr = ''

# 메인 코드 #
if __name__ == '__main__' :
    main()
