# 1. 텍스트 파일 읽기

# 1) read() 메소드
# file.read(size)
# 파일로부터 데이터를 읽어 들이는 메소드
# 텍스트 모드와 바이너리 모드에서 다른 방식으로 동작

# 반환값: 텍스트 모드/ 읽어 들인 문자열, 바이너리 모드/ 읽어 들인 바이트열
# 매개변수 size : 텍스트 모드 / 읽어 들일 최대 문자의 개수, 바이너리 모드 / 읽어 들일 최대 바이트수
# 매개변수 size 생략: 파일 전체 읽음
# 파일의 끝에 도달: 빈 문자열 ('') 반환

file = open('../2026-1-15/input/hello.txt', 'rt')
str = file.read()
print(str)
file.close()

# read() 메소드를 통해서 전체를 읽으려면 그 만큼의 메모리 공간을 필요
# 읽어야 할 파일이 크다면 일부만 읽어 들이는 작업을 반복하는 반복문을 이용해서
# 파일 전체를 읽도록 구현하는 것이 좋음
print()
file = open('../2026-1-15/input/hello.txt', 'rt')
while True:
    str = file.read(5)
    if not str:
        break
    print(str)
file.close()
# file.read(5)는 파일로부터 최대 5글자를 읽어 들임
# 파일이 종료되어 더 이상 읽어 들일 글자가 없으면 빈 문자열('')를 읽어 들임

# 2) readline() 메소드
# 텍스트 파일을 한 줄씩 읽어서 처리하는 메소드
# 파일이 종료되어 더 이상 읽어 들일 글자가 없으면 빈문자열('')를 읽어 들임
# 반복문을 이용해서 여러 번 읽어 들어야 파일 전체를 읽어 들일 수 있음
print()
file = open('../2026-1-15/input/hello.txt', 'rt')
while True:
    str = file.readline(0)
    if str == '':
        break
    print(str, end='')
file.close()

# 3) readlines() 메소드
# 라인 line 하나가 아니라 전체 라인 lines를 모두 읽어 각 라인 line 단위로 리스트에 저장하는 메소드
print()
file = open('../2026-1-15/input/hello.txt', 'rt')

line_list = file.readlines()
print(line_list)
for line in line_list:
    print(line, end='')

file.close()
