# Find the longest common subsequence shared by two strings
# This subsequence does not have to be contiguous


def LCS(s1: str, s2: str):
    
    arr = [[0]  * (n+1) for _ in range(m + 1)]
    
    for i in range(1, len(sq) + 1):
        for j in range(1, len(sq) + 1:
            if match(s1, s2, i, j):
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
                
    lcs = ""

    p = len(s1)
    q = len(s2)
    
    while i > 0 and j > 0:
        if match(s1, s2, i, j):
            lcs += s1[i-1]
            p -= 1
            q -= 1
        elif arr[i-1][j] > arr[i][j-1]:
            p -= 1
        else:
            q -= 1
            
    return lcs[::-1]
