a = str(input())
lst = [-1]*26
for i in range(len(a)):
    if lst[ord(a[i]) - ord('a')] == -1:
        lst[ord(a[i]) - ord('a')]= i

print(*lst)