# 함수 #
def main() :
    
    if x < '2' :
        print("2/8/10/16진수 입니다")
    elif x < '8' :
        print("8/10/16진수 입니다")
    elif x < '10' :
        print("10/16진수 입니다")
    elif x < '16' :
        print("16진수 입니다")
    else :
        print("입력된 값이 너무 높습니다")
    

# 전변수 #
x = input("값을 입력하면 16, 10, 8, 2진수 안에 들어가는지 판별합니다 : ")

# 메인 코드 #
if __name__ == "__main__" :
    main()
