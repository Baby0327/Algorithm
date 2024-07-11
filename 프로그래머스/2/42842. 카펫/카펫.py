def solution(brown, yellow):
    total = brown + yellow      # 전체 카펫 격자 수

    # 각 격자 수는 최소 1이기 때문에 카펫의 한 변은 최소 3 이상임을 반영
    for i in range(3, (total // 3) + 1):
        # 나누어떨어지고, 계산식이 성립한다면 내림차순의 결과값 반환
        if total % i == 0:
            j = total // i
            if (i - 2) * (j - 2) == yellow:
                return sorted([i, j], reverse=True)