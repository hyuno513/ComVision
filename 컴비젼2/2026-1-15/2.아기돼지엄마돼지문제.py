# 동요 '엄마돼지 아기돼지'의 가사가 저장되어 있는 '엄마돼지아기돼지.txt'파일을 읽어서
# '꿀' 이라는 글자가 몇 번 나오는지 찾는 프로그램

file = open('../2026-1-15/input/엄마돼지아기돼지.txt', 'rt')

# while True:
#     str = file.read(1)
#     i = 0
#     if str == '꿀':
#         i += 1
#     print(str)
#     else:
#         break
# print(i)
# file.close()
# i = 0
# while True:
#     str = file.read(1)
#     if not str:
#         if str == '꿀':
#             i += 1
#         break
#
#     print(str)
#     print(i)
# file.close()

line_list = file.readlines()
print(line_list)
count = 0
for line in line_list:
    for ch in line:
        # print(ch)
        if ch == '꿀':
            count += 1

print(f'꿀은 전체 {count}번 나타납니다.')

