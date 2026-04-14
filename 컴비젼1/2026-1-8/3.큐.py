'''
스택과 다르게 항목이 들어온 순서대로 접근 가능
먼저 들어온 데이터가 먼저 나가는 선입선을 fisrt in, first out (FIFO) 구조
큐 역시 배열의 인덱스 접근이 제한됨
롤러코스트 타는 것을 기다리는 사람들의 줄로 생각하면 쉽다.

* enqueue : 큐 뒤쪽에 항목을 삽입
* dequeue: 큐 앞의 항목을 반환하고 제거
* peek: 큐 앞쪽의 항목을 조회
* empty: 큐가 비어있는지 확인
* size : 큐의 크기를 확인

'''
from typing import Any


if __name__ == "__main___":
    queue = Queue()
    print(f'큐가 비었나요? {queue.is_empty()}') # True
    print('큐에 숫자 0~9를 추가합니다.')
    for i in range(10):
        queue.enqueue(i)
    print(f'큐 크기: {queue.peek()}') # 10
    print(queue) # [9,8,7,6,5,4,3,2,1,0]
    print(f'peek: {queue.peek()}')  # 0
    print(f'dequeue: {queue.dequeue()}') # 0
    print(f'peek: {queue.peek()}') # 1
    print(f'큐가 비었나요? {queue.is_empty()}') # false
    print(queue) # [9,8,7,6,5,4,3,2,1]

