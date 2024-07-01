import sys
sys.setrecursionlimit(10**9)

def order(left, right):
    if left > right:
        return
    else:
        # 모든 원소가 루트노드보다 작은 경우, 오른쪽 노드(서브트리)가 없음을 표시하기 위한 기본값
        mid = right + 1

        for i in range(left + 1, right + 1):
            if num[left] < num[i]:
                mid = i     # 루트노드 설정
                break

        # 왼쪽 서브트리 탐색
        order(left + 1, mid - 1)
        # 오른쪽 서브트리 탐색
        order(mid, right)
        # 탐색 끝나면 루트값 출력
        sys.stdout.write(str(num[left]) + "\n")


num = []
while True:
    try:
        num.append(int(sys.stdin.readline()))
    except:
        break

order(0, len(num) - 1)