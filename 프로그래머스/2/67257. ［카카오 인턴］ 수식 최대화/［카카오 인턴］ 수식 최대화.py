from itertools import permutations

def solution(expression):
    def calc(a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        else:
            return a * b

    nums = []
    ops = []

    num = ''
    for ch in expression:
        if ch.isdigit():
            num += ch
        else:
            nums.append(int(num))
            ops.append(ch)
            num = ''
    nums.append(int(num))  # 마지막 숫자

    answer = 0
    op_kind = list(set(ops))  # 실제 등장한 연산자 종류만

    for order in permutations(op_kind):
        temp_nums = nums[:]
        temp_ops = ops[:]

        for op in order:
            new_nums = [temp_nums[0]]
            new_ops = []

            for i in range(len(temp_ops)):
                if temp_ops[i] == op:
                    new_nums[-1] = calc(new_nums[-1], temp_nums[i + 1], op)
                else:
                    new_ops.append(temp_ops[i])
                    new_nums.append(temp_nums[i + 1])

            temp_nums = new_nums
            temp_ops = new_ops

        answer = max(answer, abs(temp_nums[0]))

    return answer


expression = "100-200*300-500+20"
print(solution(expression))