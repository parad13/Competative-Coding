def breakingRecords(s):
    min_n = s[0]
    max_n = s[0]
    min_c = 0
    max_c = 0
    
    for i in scores:
        if i > max_n:
            max_n = i
            max_c += 1
        elif i < min_n:
            min_n = i
            min_c += 1
            
    return max_c, min_c


