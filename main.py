from waypoint import Waypoint
from step import Step
from task import Task
from routine import Routine

import concurrent.futures
import time

"""
The main program for the CLI prototype

On start, prompts user for inputs, creates Waypoints, Steps, Tasks, and Waypoints
"""
# Dictionary for reference
Waypoints = {
    "Bathroom": {
        "Bathroom": Waypoint("Bathroom","Waypoint in bathroom","Bathroom"),
        "Sink": Waypoint("Sink","Waypoint at bathroom sink","Bathroom"),
        "Shower": Waypoint("Sink","Waypoint at bathroom sink","Bathroom")
    },
    "Kitchen": {
        "Sink": Waypoint("Kitchen Sink","Waypoint at kitchen sink","Kitchen"),
        "Dishwasher": Waypoint("Dishwasher", "Waypoint at dishwasher", "Kitchen")
    },
    "Bedroom": {
        "Bedroom": Waypoint("Bedroom","Waypoint at bedroom door", "Bedroom"),
        "Night Stand": Waypoint("Night Stand", "Waypoint at bedroom nightstand", "Bedroom"),
        "Bed": Waypoint("Bed","Waypoint at bed","Bedroom")
    }
}

# Dictionary
Steps = {
    
        "Go Bathroom": Step("Go to Bathroom","Go to the bathroom Waypoint",Waypoints["Bathroom"]["Bathroom"]),
        "Brush Teeth": Step("Bush Teeth","Brush teeth",Waypoints["Bathroom"]["Sink"]),
        "Floss": Step("Floss","Floss teeth",Waypoints["Bathroom"]["Sink"]),
        "Shower": Step("Shower","Take a shower",Waypoints["Bathroom"]["Shower"]),
        "Clean Shower": Step("Clean Shower","Spray and scrub shower",Waypoints["Bathroom"]["Shower"]),
    
    
        "Go Kitchen": Step("Go to Kitchen","Go to kitchen Waypoint",Waypoints["Kitchen"]["Sink"]),
        "Clean Dishes": Step("Clean Dishes","Clean, dry, put away dishes", Waypoints["Kitchen"]["Sink"]),
        "Run Dishwasher": Step("Run Dishwasher","Load, fill, and run the dishwasher", Waypoints["Kitchen"]["Dishwasher"]),

    
        "Go Bedroom": Step("Go to Bedroom","Go to bedroom Waypoint",Waypoints["Bedroom"]["Bedroom"]),
        "Read": Step("Read Book", "Read book",Waypoints["Bedroom"]["Night Stand"]),
        "Sleep": Step("Go to Sleep", "Get in bed and sleep",Waypoints["Bedroom"]["Bed"])
    
}
Tasks = {
    "Brush and Floss": Task("Brush and Floss","Brush and floss teeth",[Steps["Go Bathroom"],Steps["Floss"],Steps["Brush Teeth"]]),
    "Shower": Task("Shower", "Take a shower then clean shower", [Steps["Go Bathroom"],Steps["Shower"],Steps["Clean Shower"]]),
    "Sleep": Task("Sleep", "Read and go to bed",[Steps["Go Bedroom"],Steps["Read"],Steps["Sleep"]])
}

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

    return routine
   

def main():

    #routine = createRoutine()
    routine = Routine("Sleep Routine","Routine before going to sleep",[Tasks["Brush and Floss"],Tasks["Shower"],Tasks["Sleep"]])

    # Create a thread to check for Waypoints
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=1)

    # Follow Routine
    print("FOLLOW")
    print("Starting {}".format(routine.name))
    print(routine.description)
    for task in routine.tasks:
        print("Task: {}".format(task.name))
        for step in task.steps:
            print(step.name)
            # New thread to notify every 30 seconds
            # pool.submit(timer)
            step.waypoint.scan() # Program cannot continue until scan comes back
            
            
if __name__ == "__main__":
    main()