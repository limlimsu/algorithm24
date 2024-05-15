import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair(p):
    n = len(p)
    mindist = float("inf")
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(p[i], p[j])
            if dist < mindist:
                mindist = dist
    return mindist

def strip_closest(strip, d):
    min_dist = d
    strip.sort(key=lambda point: point[1]) 
    
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            min_dist = min(min_dist, distance(strip[i], strip[j]))
            j += 1
    
    return min_dist

def closest_pair_dist(P, n):
    if n <= 3:
        return closest_pair(P)
    
    mid = n // 2
    mid_x = P[mid][0]
    
    dl = closest_pair_dist(P[:mid], mid)
    dr = closest_pair_dist(P[mid:], n-mid)
    d = min(dl, dr)
    
    Pm = []
    for i in range(n):
        if abs(P[i][0] - mid_x) < d:
            Pm.append(P[i])
            
    ds = strip_closest(Pm, d)
    return min(d, ds)

p = [(2, 3), (12, 39), (40, 50), (4, 1), (12, 4), (3, 4)]
p.sort(key=lambda point: point[0])
print("가장 가까운 두 점의 거리:", closest_pair_dist(p, len(p)))