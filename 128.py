def consecutivenum(nums):
    sett=set(nums)
    longg=0
    for i in sett:
        if i-1 not in sett:
            length=1
            while i+length in sett:
                length = length +1
            longg= max(longg,length)
    return longg


nums = list(map(int,input().split()))
print(consecutivenum(nums))