s=input("enter the string")
left = 0
answer = 0
seen=set()
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left = left +1

    seen.add(s[right])
    answer = max(answer,right - left +1)

print(answer)
