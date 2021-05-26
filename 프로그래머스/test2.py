from collections import deque


def compare(current, word):
    cnt = 0
    for letter in word:
        if letter in current:
            cnt += 1
    if cnt == len(current)-1:
        return True
    else:
        return False
    
def bfs(begin, target, words):
    queue = deque()
    queue.append((begin, 0))
                 
    while queue:
        current, level = queue.popleft()

        if current == target:
            return level
            break

        next_node = [word for word in words if compare(current, word)]

        for node in next_node:
            queue.append((node, level+1))

    
def solution(begin, target, words):
                 
    if target not in words:
        return 0
    
    answer = bfs(begin, target, words)
    
    return answer

if __name__ == '__main__':
    result = solution("hit","cog",['cog', 'log', 'lot', 'dog', 'dot', 'hot'] )
    print(result)