import sys

def chk_password(password):
    case1 = ['a', 'e', 'i', 'o', 'u']
    check = ""

    for i in password:
        if i in case1:
            check += "a"
        else:
            check += "b"

    # 패스워드 길이가 1~20자가 아니면 False
    if len(password) < 1 or len(password) > 20:
        return False

    # a,e,i,o,u 미포함 하는가
    if not any(ch in password for ch in case1):
        return False

    # 모음이 3개 혹은 자음이 3개 연속으로 오면 안됨
    if "aaa" in check or "bbb" in check:
        return False

    # 같은 글자가 연속적으로 두번 오면 안되나 ee oo는 허용
    for i in range(1, len(password)):
        if password[i] == password[i - 1] and password[i] not in ['e', 'o']:
            return False

    return True

while 1:
    password = sys.stdin.readline().rstrip()
    if password == "end":  # 마지막 테스트 케이스
        break

    res = chk_password(password)

    if res:
        print("<%s> is acceptable." % password)
    else:
        print("<%s> is not acceptable." % password)
