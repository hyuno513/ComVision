# 파일 출력 output

# 1. 텍스트 파일 생성하기
file = open('../2026-1-13/output/hello.txt', 'wt')

file.write('안녕하세요')
file.write('\n') # \n : 개행문자: 줄을 한칸 내린다.
file.write('반갑습니다')
file.write('\n')
file.write('hello.txt 파일이 생성되었습니다.')

file.close()


# 파일의 내용을 출력할 대는 write()메소드 사용
# write() 메소드는 print()함수와 달리 자동으로 줄 바꿈 처리를 하지 않기 때문에
# 줄 바꿈이 필요한 경우 강제로 줄바꿈 문자('\n')를 삽입

# 2. 텍스트 파일에 내용 추가하기
# 기존 파일에 내용을 추가할 수 있는 모드는 a모드

file = open('./output/hello.txt', 'at') # 텍스트로 추가
file.write('Hello.\n')
file.write('Nice to meet you.\n')
print('hello.txt 파일에 새로운 내용이 추가되었습니다.')
file.close()


# 한글 이름 파일 utf-8로 문서 작성하기
import codecs

file = codecs.open('./output/한글파일.txt', 'w','utf-8')
file. write('안녕하세요.')
file.close()