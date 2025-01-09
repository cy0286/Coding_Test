T = int(input())

for test_case in range(1, T + 1):
	N = int(input())
	money = list(map(int, input().split()))
	average = sum(money) / N
	num = sum(1 for i in money if i <= average)
	print(f"#{test_case} {num}")