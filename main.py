from waypoint import Waypoint
from step import Step
from task import Task
from routine import Routine

"""
The main program for the CLI prototype

On start, prompts user for inputs, creates Waypoints, Steps, Tasks, and Waypoints
"""

Waypoints = {}
Steps = {}
Tasks = {}
Routines = {}

def createWaypoint() -> Waypoint: # A function to get user input and make a Waypoint object
    # Make a Waypoint, create a Step, add to steps list
    waypoint_name = input("Waypoint Name: ")
    waypoint_description = input("Waypoint Description: ")
    waypoint_location = input("Waypoint Location: ")
    waypoint = Waypoint(waypoint_name,waypoint_description,waypoint_location)
    return waypoint

def createStep(waypoint: Waypoint) -> Step: # A function to get user inputs and make a Step object
    step_name = input("Step Name: ")
    step_description = input("Step Description: ")
    step = Step(step_name,step_description,waypoint)
    return step

def createTask() -> Task: # A function to get user inputs and make a Task object
    task_name = input("Task Name: ")
    task_description = input("Task Description: ")
    return task_name,task_description


def createRoutine() -> Routine: # A function to get user inputs and make a Routine object
    pass

def main():
    print("CREATE")
    print("Make a routine:")
    # Get info for routine
    routine_name = input("Routine Name: ")
    routine_description = input("Routine Description: ")

    tasks = []
    # Loop add Tasks  
    task_limit = 3 # 3 task limit for testing
    for i in range(0,task_limit):
        task_details = createTask()

        steps = []
        # Loop add Step 
        for j in range(0,task_limit):

            # Make a Waypoint, create a Step, add to steps list
            waypoint = createWaypoint()
            Waypoints[waypoint.name] = waypoint
            step = createStep(waypoint)
            Steps[step.name] = step
            steps.append(step) 
        
        # Make a Task, add to task list
        task = Task(task_details[0],task_details[1],steps)
        Tasks[task.name] = task
        tasks.append(task)

    # make Routine
    routine = Routine(routine_name,routine_description,tasks)
    Routines[routine.name] = routine
    
    # Follow Routine
    print("FOLLOW")
    print("Starting {}".format(routine_name))
    print(routine_description)
    for task in routine.tasks:
        print("Task: {}".format(task.name))
        for step in task.steps:
            print(step.name)
            step.waypoint.scan()













if __name__ == "__main__":
    main()