# % 연산자
name = 'Kai'
print('내 이름은 %s입니다' % name) # 내이름은 Kai입니다. / $s : string
print('내 이름은', name, '입니다', sep='')
print('내 이름은' + name + '입니다.')

height = 175.8
print('내 키는 %fcm입니다' % height) # 내 키는 175.8000000000cm입니다. / %f : float

year, month, day = 2025, 12, 16
print('오늘은 %d년 %d월 %d일 입니다.') % (year, month, day)
# 오늘은 2025년 12월 16일 입니다. / %d : decimal(십진법)

