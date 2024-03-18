from component import Component
from waypoint import Waypoint
from step import Step


""" 
This class is the intermediary component of the program
Steps -> *Tasks* -> Routines

Tasks are Components that hold a group of Steps. 
Tasks have a priority attribute that allows the user to designate its relative 
importance compared to other tasks. Tasks correspond to a singe full activity: 
arrival at, execution of, and completion. Tasks have Steps associated with them 
to break them to chunks. Tasks, once started, require the user to check in by 
rescanning the Waypoint to show that they're still there. Tasks are completed 
by holding the scanner to the Waypoint for 5 seconds. Tasks share a many to many 
relationship with Routines. 

- Task Name
- Task Description
- Task Priority
- Steps List
"""

class Task(Component):
    def __init__(self, name, description, steps: list):
        super().__init__(name, description)
        self.steps = steps
        # TODO Add priority attribute

    def toString(self):
        return("Name: {} | Description: {} | Steps: ({})".format(self.name,self.description, [step.toString() for step in self.steps]))
    
    def do(self):
        print(self.toString())
        print()
        for step in self.steps:
            step.do()

def main():
    waypoint_a = Waypoint("test Waypoint","test Waypoint description","test location")
    step_one = Step("Step 1","Step 1 description",waypoint_a)
    step_two = Step("Step 2","Step 2 description",waypoint_a)
    test_task = Task("Test Task", "This is a test Task", [step_one,step_two])
    print(test_task.toString())

if __name__=="__main__": 
    main()