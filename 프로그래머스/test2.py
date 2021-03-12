def solution(citations):
    # h = 0
    citations.sort(reverse= True)
    
    for i, citation in enumerate(citations):
        h = len(citations[:i])
        if citation >= h:
            h += 1
        else:
            break
        
    return h

if __name__ == '__main__':
    result = solution([10, 50, 100])
    print(result)