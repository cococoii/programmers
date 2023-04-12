#deque 사용
from collections import deque
#위,오른쪽,아래,왼쪽으로 이동
d = [(1,0),(0,1),(-1,0),(0,-1)]
def solution(maps):
    answer = bfs(maps,0,0) #시작값이 0,0이므로
    if answer==1: #도달하지 못한 경우에는 maps의 값이 1이 될 수 밖에 없다
        return -1
    return answer

def bfs(maps,y,x): #BFS
    queue = deque()
    queue.append((y,x)) #지금 처음 시작값
    while queue:
        y1,x1 = queue.popleft() #queue 값 꺼내기
        for dx,dy in d: #위,오른쪽,아래,왼쪽으로 이동
            if 0<=y1+dy<len(maps) and 0<=x1+dx<len(maps[0]): #사각형 안에 있어야함
                if maps[y1+dy][x1+dx]==1:#visted하지 않은 경우
                    maps[y1+dy][x1+dx]=maps[y1][x1]+1 #이동한 거리 +1
                    queue.append((y1+dy,x1+dx)) #그때의 값 대입
    return maps[len(maps)-1][len(maps[0])-1] # 가장 끝에 있는 값 return

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])