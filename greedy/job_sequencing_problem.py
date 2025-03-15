
# Problem: https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

# https://www.youtube.com/watch?v=QbwltemZbRg



class Solution:
    # Function used for sorting jobs according to their deadlines
    def JobSequencing(self, id, deadline, profit):
        jobs = sorted(zip(id, deadline, profit), key=lambda x:x[2], reverse=True)
        
        max_deadline = max(deadline)
        time_slots = [-1] * (max_deadline + 1)
        max_profit = 0
        jobs_count = 0

        for job_id, d, p in jobs:
            for j in range(d, 0, -1):
                if time_slots[j] == -1:
                    time_slots[j] = job_id
                    max_profit += p
                    jobs_count += 1
                    break
        return (jobs_count, max_profit)

