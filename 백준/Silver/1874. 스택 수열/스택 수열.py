import sys

def stack_sequence(n, sequence):
    stack = []
    res = []
    current = 1  # push할 숫자 (1~n순으로 진헹)
    for num in sequence:
        while current <= num:  # 필요한 숫자까지 push
            stack.append(current)
            res.append('+')
            current += 1
        if stack and stack[-1] == num:  # 스택의 top이 num과 같으면 pop
            stack.pop()
            res.append('-')
        else:
            return ['NO']
    return res


n = int(sys.stdin.readline().rstrip())
sequence = [int(input()) for _ in range(n)]  # 수열 입력

output = stack_sequence(n,sequence)
print("\n".join(output))





