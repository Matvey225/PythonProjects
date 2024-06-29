def say_sequence(n):
    if n <= 0:
        return "Неверный ввод. n должен быть положительным числом и больше 0."
    sequence = "1"
    
    for _ in range(n - 1):  
        next_sequence = ""
        count = 1
        answer = ''
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i - 1]:
                count += 1
            else:
                next_sequence += str(count) + sequence[i - 1]
                count = 1
        next_sequence += str(count) + sequence[-1]  
        sequence = next_sequence
        index = sequence.find(str(x))
        for j in range(index, len(sequence)):
            answer += sequence[j]
    return answer

index = 0
x, n = map(int, input().split())
result = say_sequence(n)
print(result)