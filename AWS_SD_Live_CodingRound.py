"""
There are two methods of a class Schedular, one method is to submit a job, which takes a tuple as an argument. One value in tuple is a job name,
and another value is the weight of that job, which is in integer. If a job is submitted already, the weight gets added in the existing job.
Another method is select, when it is called, it returns a job with maximun weight each time. For each call, it returns job with maximum weight.
"""

class Schedular:

    def __init__(self):
        self.job_dict = {}

    def submit(self, job):
        if job[0] in self.job_dict.keys():
            self.job_dict[job[0]] = self.job_dict[job[0]] + job[1]
            
        else:
            self.job_dict[job[0]] = job[1]
            # print(self.job_dict)

    def select(self):
        max_job = list(self.job_dict.keys())[0]
        max_weight = 0
        for i in self.job_dict.keys():
            if self.job_dict[i]> max_weight:
                max_weight = self.job_dict[i]
                max_job = i
        
        self.job_dict.pop(max_job)
        print(self.job_dict)
        return max_weight
            


s = Schedular()
s.submit(("A", 3))
s.submit(("B", 4))
s.submit(("C", 1))
s.submit(("D", 7))
s.submit(("E", 9))
s.submit(("A", 2))
s.submit(("D", 8)) 

print(s.select()) # Output D = 15
print(s.select()) # Output E = 9
print(s.select()) # Output A = 5

t = Schedular()
t.submit(("J", 45))
t.submit(("G", 44))
print(t.select()) # Output B = 4
# s.select() # Output C = 1 