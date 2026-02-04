s = input().strip()
print("".join(ch.lower() if ch.isupper() else ch.upper() for ch in s))
