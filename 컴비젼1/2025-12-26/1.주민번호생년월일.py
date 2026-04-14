# 주민등록번호에서 생년월일 6자리를 추출하는 프로그램
# 사용자로부터 하이픈을 포함한 전체 주민등록번호를 입력받아 처리하는데
# 만약 하이픈의 위치가 올바르지 않다면 오류 메시지를 출력하고 다시 입력받도록 처리

a = input('하이픈을 포함하여 전체 주민등록번호를 입력>>>')
a2 = a.split('-')
print(a2)
print(len(a2[0]))
print(len(a2[1]))

# while True:
#     if len(a2[0]) == 6:
#         print(a2)
#         print(f'생년월일은 {a2[0]}입니다.')
#     break
#     else: print("하이픈의 위치가 잘못되었습니다.")

while True:
    p = input('주민번호입력')
    if p.find('-') != 6:
        print('하이픈의 위치 잘못')
        continue
    birthday = p.split('-')
    print(birthday)
    print(f'생년월일은 {birthday[0]}입니다.')
    break