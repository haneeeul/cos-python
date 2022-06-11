def solution(num):
	answer = ''
	num_str = str(num + 1)
	for i in num_str:
		if str(i) == '0':
			answer += '1'
		else:
			answer += str(i)
	return int(answer)

num = 9949999
ret = solution(num)

print("solution 함수의 반환 값은", ret, "입니다.")