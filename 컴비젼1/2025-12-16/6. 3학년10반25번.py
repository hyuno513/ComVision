# 5자리로 구성된 학번 '31025'를 학년, 반, 번호로 나누어 출력하는 프로그램을 구현
# 실행 예)
# 3학년 10반 25번

student = '31025'
grade_no = student[0:1]
class_no = student[1:3] # [-4:-2]
stu_no = student[3:5] # [-2:]
print(grade_no, '학년', class_no, '반', stu_no, '번')