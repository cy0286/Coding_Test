T = int(input())

for test_case in range(1, T + 1):
	word = input()
	result = ''
	for i in range(len(word)):
		if word[i] not in 'aeiou':
			result += word[i]
	print(f"#{test_case} {result}")