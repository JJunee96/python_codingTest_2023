# python_codingTest_2023
파이썬 코딩테스트 리포지토리

## 1일차
1. 코딩테스트 소개
2. 코딩테스트 학습
    - [x] 자료구조 : 배열 / 리스트
    - [x] 구간합

## 2일차
! 파이썬 파일명에는 '_' 만 사용할것!!
1. 코딩테스트 학습
    - [x] 구간합 2
    - 자료구조 다시
        - [x] 연결리스트
        - [x] 스택
        - [x] pythonds 스택 확인

## 3일차
1. 코딩테스트 학습
    - 자료구조
        - [x] 큐
        - [x] pythonds 큐 확인
        - 이진 트리
            - [x] 삭제는 연결리스트 삭제와 유사
        - [x] 그래프

## 4일차        
1. 코딩테스트 학습
    - 자료구조
        - [x] 그래프 - DFS
        - [x] 재귀호출
        - [x] 정렬 소개

## 5일차
1. 코딩테스트 학습
    - 자료구조
        - [x] 정렬
        - [x] 검색
        - [x] 다이나믹 프로그래밍 / 피보나치 실행시간 비교

## 6일차
1. 코딩테스트 학습
    - 자료구조
        - [x] deque (덱)
    - 알고리즘
        - [x] 투 포인터
        - [x] 슬라이딩 윈도우
        - [x] 정렬

```python
# 백준 11003 - 최솟값 찾기 1
from collections import deque
# from pythonds.basic.deque import Deque

N, L = map(int, input().split())    # 12 3
mydeque = deque()
now = list(map(int, input().split())) # 1 5 2 3 6 2 3 7 3 5 2 6

# 새 값이 들어올때 마다 정렬 대신 현재 수 보다 큰 값을 덱에서 제거
# 시간복잡도를 줄임
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:  # 인덱스가 현재값보다 크면
        mydeque.pop() # 빼버린다
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L:      # 범위를 벗어난 값도 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0], end = ' ') # 무조건 최소값(min() 과 동일)
```

# 7일차
1. 코딩테스트 학습
    - 자료구조
        - [x] 그래프
        - [x] PrioriyQueue (우선순위 큐)
        - [ ] heapq (힙큐)
    - 알고리즘
        - [x] 탐색 - DFS/BFS
        - [ ] 그리디
        - [ ] 정수 