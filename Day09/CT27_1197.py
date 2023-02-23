# 백준 1197 - 최소신장트리
import sys
from queue import PriorityQueue

input = sys.stdin.readline
N, M = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for i in range(M):
    s, e, w = map(int, input().split())
    pq.put((w, s, e))

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):    # 두 노드 연결
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0

while useEdge < N - 1: # MST는 항상 N-1
    w, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += w
        useEdge += 1 # 중요 !! 사이클 생긴 엣지값은 + 1 X

print(result)