def solution(triangle):
    for idx, val in enumerate(triangle):
        if idx == 0:
            continue
        for i, num in enumerate(val):
            if i == 0:
                val[0] += triangle[idx-1][0]
            if i == idx:
                val[i] += triangle[idx-1][-1]
            if i != 0 and i!=idx:
                val[i] += max(triangle[idx-1][i], triangle[idx-1][i-1])
        
    return max(triangle[-1])