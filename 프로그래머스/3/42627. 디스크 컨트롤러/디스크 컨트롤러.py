import heapq

def solution(jobs):
    pq = []
    n = len(jobs)
    jobs.sort(key=lambda x: x[0])

    cur_time = cnt = 0
    total_time = 0
    i = 0
    while i < n:
        while cnt < n and jobs[cnt][0] <= cur_time:
            heapq.heappush(pq, (jobs[cnt][1], jobs[cnt][0], cnt))
            cnt += 1

        if pq:
            d, s, _ = heapq.heappop(pq)
            cur_time += d
            total_time += (cur_time - s)
            i += 1
        else:
            cur_time = jobs[cnt][0]

    return (total_time // n)