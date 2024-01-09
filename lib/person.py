#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
# Person and lib/person.py
# Define a name property for your Person class. The name
#    must be of type str and between 1 and 25 characters. The name should be converted to title caseLinks to an external site.
# before it is saved. Your __init__ method should receive a default argument for name.
# If the name is invalid, the setter method should print() "Name must be string between 1 and 25 characters."
class Person:
    def __init__(self, name='tyler', job='Marketing'):
        self.name = name
        self.job = job
    def get_name(self):
        return self._name
    def set_name(self, name):
        if isinstance(name, str) and 1<= len(name) <= 25:
            title_name = name.title()
            self._name = title_name
        else:
            print('Name must be string between 1 and 25 characters.')
    name= property(get_name, set_name)
        
    
#     Define a job property for your Person class. Your __init__ method should receive a default argument for job.
# If the job is invalid, the setter method should print() "Job must be in list of approved jobs." 
# The job must be in the following list of jobs:
    def get_job(self):
        return self._job
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
    job= property(get_job, set_job)