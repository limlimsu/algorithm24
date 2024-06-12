import heapq

def make_huffman_tree(freq, label):
    n = len(freq) # 문자의 개수
    h = [] # 힙을 위한 리스트

    # 모든 문자를 최소 힙에 삽입
    for i in range(n):
        heapq.heappush(h, (freq[i], label[i]))

    # n-1번 반복
    for i in range(1, n):
        e1 = heapq.heappop(h) # 가장 작은 트리
        e2 = heapq.heappop(h) # 다음 작은 트리
        heapq.heappush(h, (e1[0] + e2[0], (e1, e2))) # 새로운 트리 삽입

    return heapq.heappop(h) # 최종 트리 반환

# 테스트 예제
freq = [5, 9, 12, 13, 16, 45]
label = ['a', 'b', 'c', 'd', 'e', 'f']
huffman_tree = make_huffman_tree(freq, label)
print(f"Huffman Tree: {huffman_tree}")