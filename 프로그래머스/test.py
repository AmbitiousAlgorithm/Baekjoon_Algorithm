import heapq
from collections import deque

def solution(reqs):
    answer = []
    wait = []

    reqs = deque([(-rank,time,idx) for idx,(rank,time) in enumerate(reqs,1)])
    RANK, TIME, IDX = 0, 1, 2
    heapq.heappush(wait, reqs.popleft())
    
    def nowait(wait):
        if not wait and reqs:
            heapq.heappush(wait, reqs.popleft())
    time = 0

    while wait:
        running = heapq.heappop(wait)
        end = running[TIME]
        answer.append(running[IDX])
        for _ in range(end):
            time += 1 
            if time % 3 == 0 and reqs:
                heapq.heappush(wait, reqs.popleft())

        nowait(wait)
    return answer

print(solution(	[[158, 2], [40, 5], [14, 4], [206, 5]]))


# import heapq
# from collections import deque

# def solution(reqs):
#     answer = []
#     wait = []

#     reqs = deque([(-rank,time,idx) for idx,(rank,time) in enumerate(reqs,1)])
#     RANK, TIME, IDX = 0, 1, 2
#     heapq.heappush(wait, reqs.popleft())
    
#     def nowait(wait):
#         if not wait and reqs:
#             heapq.heappush(wait, reqs.popleft())
#     time = 0

#     while wait:
#         running = heapq.heappop(wait)
#         end = running[TIME]
#         answer.append(running[IDX])
#         for _ in range(end):
#             time += 1 
#             if time % 3 == 0 and reqs:
#                 heapq.heappush(wait, reqs.popleft())

#         nowait(wait)
#     return answer