def solution(skill, skill_trees):
    answer = 0
    level = 0
    for s in skill_trees:
        for i in range(len(s)):
            if i == len(s)-1:
                if s[i] not in skill:
                    answer+=1
                else:
                    if s[i] == skill[level]:
                        answer+=1
            elif i!=len(s) and s[i] in skill:
                if s[i] == skill[level]:
                    level+=1
                    continue
                else:
                    break

        level = 0

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill,skill_trees))