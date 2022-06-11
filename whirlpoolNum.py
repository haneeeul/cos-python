def in_range(i, j, n):
	return 0 <= i and i < n and 0 <= j and j < n

def solution(n):
	answer = 0
	board = [[0 for j in range(n)] for i in range(n)] # [[0]*n]*n 불가능
  # 소용돌이 방향에 맞춰서
  dy = [0, 1, 0, -1]
  dx = [1, 0, -1, 0]
	ci, cj = 0, 0
	num = 1
	while in_range(ci, cj, n) and board[ci][cj] == 0:
		for k in range(4):
      # 범위를 벗어나는 경우에는 break
			if not in_range(ci, cj, n) or board[ci][cj] != 0:
				break
			while True:
        # 한번 정해진 방향으로 쭉 간다(무한루프)
				board[ci][cj] = num
				if ci == cj:
					answer += num
				num += 1
				ni = ci + dy[k]
				nj = cj + dx[k]
				if not in_range(ni, nj, n) or board[ni][nj] != 0:
          # 방향 전환
					ci += dy[(k + 1) % 4]
					cj += dx[(k + 1) % 4]
					break
				ci = ni
				cj = nj
	return answer

n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")