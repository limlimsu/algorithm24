NO_OR_CHARS = 128
def shift_table(pat):
    m = len(pat)
    tbl = [m]*NO_OR_CHARS
    
    for i in range(m-1):
        tbl[ord(pat[i])] = m-1-i

    return tbl

def search_horspool(T, P):
    m = len(P)
    n = len(T)
    t = shift_table(P)
    i = m-1
    while(i <= n-1):
        k = 0
        while k <= m-1 and P[m-1-k]==T[i-k]:
            k += 1
        if k == m :
            return i-m+1
        else :
            tc = t[ord(T[i-k])]
            i += max(1, (tc-k))
    return -1

print("패턴의 위치", search_horspool("PEACHPINEAPPLEGRAPE", "GRAPE"))

