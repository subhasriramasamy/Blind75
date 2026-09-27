s = 'aaa'
res = []
count= 0
for i in range(len(s)):
    l,r = i,i
    while l>=0 and r<len(s) and s[l] == s[r]:
        res.append(s[l:r+1])
        count += 1
        l -= 1
        r += 1 

for i in range(len(s)):
    l,r = i,i+1
    while l>=0 and r<len(s) and s[l] == s[r]:
        res.append(s[l:r+1])
        count += 1
        l -= 1
        r += 1

print(res)
print(count)