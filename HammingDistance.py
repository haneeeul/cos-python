'''
해밍 거리란 같은 길이를 가진 두 개의 문자열에서
같은 위치에 있지만 서로 다른 문자의 개수를 뜻한다.
'''
def func_a(string, length):
	padZero = ""
	padSize = length - len(string)
	for i in range(padSize):
		padZero += "0"
	return padZero + string

def solution(binaryA, binaryB):
	# 길이가 더 긴 2진수 문자열의 길이를 구한다.
  max_length = max(len(binaryA), len(binaryB))
	# 더 짧은 문자열의 앞에 0을 채워 넣어 길이를 맞춘다.
  binaryA = func_a(binaryA, max_length) # parameter (string, int) 이므로 길이를 구하기 위해서는 len() 사용
	binaryB = func_a(binaryB, max_length)
  # 길이가 같은 두 2진수 문자열의 해밍 거리를 구한다.
	hamming_distance = 0
	for i in range(max_length):
		if binaryA[i] != binaryB[i]:
			hamming_distance += 1
	return hamming_distance