class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs, max_deadline):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)
    n = len(jobs)
    result = [None] * max_deadline  # Result array to store job sequence
    slot = [False] * max_deadline   # Free time slots

    total_profit = 0
    for job in jobs:
        # Find a free slot from job's deadline backwards
        for j in range(min(max_deadline - 1, job.deadline - 1), -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job.id
                total_profit += job.profit
                break

    return result, total_profit

# Driver code
jobs = [Job('J1', 2, 100), Job('J2', 1, 50), Job('J3', 2, 10), Job('J4', 1, 20), Job('J5', 3, 70)]
max_deadline = 3
job_sequence, max_profit = job_sequencing(jobs, max_deadline)
print("Job sequence:", job_sequence)
print("Total profit:", max_profit)
