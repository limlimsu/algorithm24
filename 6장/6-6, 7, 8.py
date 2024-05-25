M = 11
table = [None]*M
def hashFn(key) :
    return key % M

def lp_insert(key) :
    id = hashFn(key)
    count = M
    while count>0 and (table[id] != None) :
        id = (id + 1 + M) % M
        count -= 1
    if count > 0 :
        table[id] = key
    return

def lp_search(key) :
    id = hashFn(key)
    count = M
    while count > 0 :
        if table[id] == None :
            return None
        if table[id] == key :
            return table[id]
        id = (id + 1 + M) % M
        count -= 1
    return None

def lp_delete(key) :
    id = hashFn(key)
    count = M
    while count > 0 :
        if table[id] == None : return
        if table[id] != -1 and table[id] == key :
            table[id] = -1
            return
        id = (id + 1 + M) % M
        count -= 1
               
print("   최초:", table)
lp_insert(30); print("30 삽입:", table)
lp_insert(18); print("18 삽입:", table)
lp_insert(12); print("12 삽입:", table)
lp_insert(22); print("22 삽입:", table)
lp_delete(18); print("18 삭제:", table)
lp_delete(12); print("12 삭제:", table)
print("22 탐색:", lp_search(22))

