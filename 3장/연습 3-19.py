import itertools #반복자 생성하고 다루는 함수들(순열, 조합등)을 포함한 내장 모듈 

def calculate_cost(assignment, jobs):
    total_cost = 0
    for job, _ in assignment: #job,_는 언패킹 기능 사용하여 작업의 비용은 무시하고 있음
        job_index = jobs.index(job)
        total_cost += jobs[job_index][1] 
    return total_cost

def job_assignment_permutation(jobs, workers):
    min_cost = float('inf')
    best_assignment = None
    
    for perm in itertools.permutations(jobs):
        assignment = list(zip(perm, workers))
        cost = calculate_cost(assignment, jobs)
        if cost < min_cost:
            min_cost = cost
            best_assignment = assignment
    
    return best_assignment, min_cost

jobs = [("Job1", 5), ("Job2", 3), ("Job3", 8)]
workers = [("Worker1",), ("Worker2",), ("Worker3",)]

best_assignment, min_cost = job_assignment_permutation(jobs, workers)
print("Best Assignments:", best_assignment)
print("Total Cost:", min_cost)

