import sys

## 함수 ##
def main() :
    intVar = 0
    floatVar = 0.0
    boolVar = True
    strVar = ''
    listVar = []
    tupleVar = ()
    dictVar = {}
    setVar = set()

    print('int형 기본 크기 --> ', sys.getsizeof(intVar))
    print('float형 기본 크기 --> ', sys.getsizeof(floatVar))
    print('bool형 기본 크기 --> ', sys.getsizeof(boolVar))
    print('str형 기본 크기 --> ', sys.getsizeof(strVar))
    print('list형 기본 크기 --> ', sys.getsizeof(listVar))
    print('tuple형 기본 크기 --> ', sys.getsizeof(tupleVar))
    print('dict형 기본 크기 --> ', sys.getsizeof(dictVar))
    print('set형 기본 크기 --> ', sys.getsizeof(setVar))

## 변수 ##
intVar, floatVar, boolVar, strVar, listVar, tupleVar, dictVar, setVar = [None] * 8

## 메인 코드 ##
if __name__ == '__main__' :
    main()

