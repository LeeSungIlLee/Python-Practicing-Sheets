# 변수 #
W50000, W10000, W5000, W1000, Wmoney = 0, 0, 0, 0, 0

# 메인 코드 #
Wmoney = int(input("교환할 액수를 입력하세요 : "))

W50000 = Wmoney // 50000
Wmoney %= 50000

W10000 = Wmoney // 10000
Wmoney %= 10000

W5000 = Wmoney // 5000
Wmoney %= 5000

W1000 = Wmoney // 1000
Wmoney %= 1000

print("50000원짜리 ==> %d개" % W50000)
print("10000원짜리 ==> %d개" % W10000)
print("5000원짜리 ==> %d개" % W5000)
print("1000원짜리 ==> %d개" % W1000)
print("잔돈 ==> %d원" % Wmoney)
