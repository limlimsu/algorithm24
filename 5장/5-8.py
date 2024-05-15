# 띠(strip) 영역 내에서 d보다 작은 최근접 쌍의 거리 찾기
def strip_closest(P, d):
    n = len(P)  # 리스트 내의 점의 수
    d_min = d  # 최소 거리를 d로 초기화

    # 리스트 P를 y 좌표에 따라 정렬
    P.sort(key=lambda point: point[1])
    
    # 모든 점들을 순회하면서 가장 가까운 거리를 찾음
    for i in range(n):
        j = i + 1
        # y 좌표의 차이가 d_min 미만인 점들만 검사
        while j < n and (P[j][1] - P[i][1]) < d_min:
            dij = distance(P[i], P[j])
            if dij < d_min:
                d_min = dij
            j += 1
    return d_min

# 거리를 계산하는 함수
def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

P = [(1, 3), (4, 4), (5, 5), (10, 10), (2, 2)]
d = 3
print("The smallest distance is:", strip_closest(P, d))