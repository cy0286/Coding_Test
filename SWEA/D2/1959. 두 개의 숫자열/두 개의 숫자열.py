T = int(input())

for test_case in range(1, T + 1):
	A, B = map(int, input().split())
	A_list = list(map(int, input().split()))
	B_list = list(map(int, input().split()))
	max_result = 0
	if A < B:
		for shift in range(B - A + 1):
			current_sum = 0
			for i in range(A):
				current_sum += A_list[i] * B_list[i + shift]
			max_result = max(max_result, current_sum)
	else:
		for shift in range(A - B + 1):
			current_sum = 0
			for i in range(B):
				current_sum += A_list[i + shift] * B_list[i]
			max_result = max(max_result, current_sum)
	print(f"#{test_case} {max_result}")