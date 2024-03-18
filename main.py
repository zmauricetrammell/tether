from component import Component
from waypoint import Waypoint
from step import Step
from task import Task
from routine import Routine

import threading
import time 

import pickle
import os
import winsound

from consolemenu import *
from consolemenu.items import *


# Empty dictionary items so temporarily store object data
Waypoints = {}
Steps = {}
Tasks = {}
Routines = {}

User_Status = "GO" # GO -> STOP

frequency = 1000  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

def createWaypoint() -> Waypoint: # A function to get user input and make a Waypoint object
    # Make a Waypoint, create a Step, add to steps list
    waypoint_name = input("Waypoint Name: ")
    waypoint_description = input("Waypoint Description: ")
    waypoint_location = input("Waypoint Location: ")
    waypoint = Waypoint(waypoint_name,waypoint_description,waypoint_location)

    # Add to Waypoints Dictionary
    Waypoints[waypoint.name] = waypoint

    # Save data with pickle
    saveData(Waypoints,"waypoints")

    # Add to waypoint menu
    new_waypoint_function_item = FunctionItem(waypoint.name,waypoint.do)
    waypoint_menu.append_item(new_waypoint_function_item)

    return waypoint

def _chooseWaypoint(name: str):
    global Waypoints
    waypoint_keys = Waypoints.keys()
    waypoint_selection_index = SelectionMenu.get_selection(waypoint_keys,"Select A Waypoint for '{}'".format(name))
    return Waypoints[list(waypoint_keys)[waypoint_selection_index]]

def createStep(waypoint: Waypoint) -> Step: # A function to get user inputs and make a Step object
    step_name = input("Step Name: ")
    step_description = input("Step Description: ")
    step = Step(step_name,step_description,waypoint)
    return step

def userCreateStep():
    step_name = input("Step Name: ")
    step_description = input("Step Description: ")
    step = Step(step_name,step_description,_chooseWaypoint(step_name))
    #print(step.toString())
    # Add to Steps Dictionary
    Steps[step.name] = step

    # Save data with pickle
    saveData(Steps,"steps")

    # Add to step menu
    new_step_function_item = FunctionItem(step.name,timeDo,[step])
    global step_menu
    step_menu.append_item(new_step_function_item)
    return step

# Selection menu to choose and append steps to task object, returns task object
def _chooseSteps():
    global Steps
    step_keys = list(Steps.keys())
    task_steps_list = [] # This list will be filled by selection menu choices

    step_counter = 1
    step_selection_index = SelectionMenu.get_selection(step_keys,"Select Step '{}'".format(step_counter)) # Use a selection menu to get a choice of step for the list
    while step_selection_index < len(step_keys):
        step_counter += 1
        task_steps_list.append(Steps[step_keys[step_selection_index]])
        step_selection_index = SelectionMenu.get_selection(step_keys,"Select Step '{}'".format(step_counter))

    return task_steps_list
    
        
def createTask() -> Task: # A function to get user inputs and make a Task object
    task_name = input("Task Name: ")
    task_description = input("Task Description: ")
    steps_list = _chooseSteps()

    # Create Task Object
    task = Task(task_name,task_description,steps_list)

    # Add to Tasks Dictionary
    Tasks[task.name] = task

    # Save data with pickle
    saveData(Tasks,"tasks")

    # Add to task menu
    new_task_function_item = FunctionItem(task.name,task.do)
    global task_menu
    task_menu.append_item(new_task_function_item)
    return task

# Selection menu to choose and append tasks to list in routine object, returns routine object
def _chooseTasks():
    global Tasks
    task_keys = list(Tasks.keys())
    routine_task_list = [] # This list will be filled by selection menu choices

    task_counter = 1
    task_selection_index = SelectionMenu.get_selection(task_keys,"Select Task '{}'".format(task_counter)) # Use a selection menu to get a choice of task for the list
    while task_selection_index < len(task_keys):
        task_counter += 1
        routine_task_list.append(Tasks[task_keys[task_selection_index]])
        task_selection_index = SelectionMenu.get_selection(task_keys,"Select Task '{}'".format(task_counter))
    
    return routine_task_list


def createRoutine() -> Routine: # A function to get user inputs and make a Routine object
    # Get info for routine
    routine_name = input("Routine Name: ")
    routine_description = input("Routine Description: ")
    tasks_list = _chooseTasks()

    # Create a routine object
    routine = Routine(routine_name,routine_description,tasks_list)

    # Add to Routine Object
    Routines[routine.name] = routine 

    # Save data with pickle
    saveData(Routines,"routines")

    # Add to routine menu
    new_routine_function_item = FunctionItem(routine.name,routine.do)
    global routine_menu
    routine_menu.append_item(new_routine_function_item)

    return routine
    
# Reminder function: prints "Reminder" ever 'interval' seconds
def reminder(interval: int):
    while User_Status == "GO":
        count = 0
        while count < interval:
            if User_Status == "STOP":
                return
            time.sleep(1)
            count +=1
        #print("Reminder")
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        
        

# Pickles 'object' parameter and saves to a file named './saved_data/[OBJECT_NAME].pkl'
def saveData(object: Component,object_name: str):
    folder_path = './saved_data/'
    #print(folder_path+object_name+'.pkl')
    with open(folder_path+object_name+'.pkl','wb') as file:
        pickle.dump(object,file)

# Checks if pickle file exists, loads data if True, return object or empty dictionary
def loadData(object_name: str) -> dict:
    folder_path = './saved_data/'
    file_path = folder_path+object_name+'.pkl'

    isExist = os.path.exists(file_path)

    if isExist:
        with open(folder_path+object_name+'.pkl','rb') as file:
            loaded_data = pickle.load(file)
            return loaded_data
    else:
        return {}

"""
Menu construct using ConsoleMenu
Includes

Routine
--List of Routines
--Create New
Task
--List of Tasks
--Create New
Step
--List of Steps
--New Step
Waypoints
--List of Waypoints
--New Waypoint
"""

# Menu object with title info 
main_menu = ConsoleMenu("Tether Main Menu", "Neurodivergence Grounding Application")

# Make Component menus
waypoint_menu = ConsoleMenu("Waypoints", "Select or Create Waypoint")
step_menu = ConsoleMenu("Steps", "Select or Create Steps")
task_menu = ConsoleMenu("Tasks", "Select or Create Tasks")
routine_menu = ConsoleMenu("Routines", "Select or Create Routines")

# Create and append the creation functions to menus
new_waypoint_function_item = FunctionItem("Create New Waypoint",createWaypoint)
new_step_function_item = FunctionItem("Create New Step",userCreateStep)
new_task_function_item = FunctionItem("Create New Task",createTask)
new_routine_function_item = FunctionItem("Create New Routine",createRoutine)

waypoint_menu.append_item(new_waypoint_function_item)
step_menu.append_item(new_step_function_item)
task_menu.append_item(new_task_function_item)
routine_menu.append_item(new_routine_function_item)   

def timeDo(step: Step): # Wrapper function to call step.do() and start timer
    timer_thread = threading.Thread(target = reminder, args = (120,)) # timer thread with 120 second interval
    global User_Status
    User_Status = "GO"
    timer_thread.start() # Start thread timer
    step.do() # Program cannot continue until scan comes back
    User_Status = "STOP"
    timer_thread.join() # Join thread to wait for it to check for the stop status

def main():
    #pass
    # Load data from saved files
    global Waypoints, Steps, Tasks
    Waypoints = loadData("waypoints")
    Steps = loadData("steps")
    Tasks = loadData("tasks")

    # Get each Waypoint, make a menu item for scan function
    for waypoint in Waypoints.values():
        waypoint_function_item = FunctionItem(waypoint.name,waypoint.do)
        waypoint_menu.append_item(waypoint_function_item)

    # Get each Step, make a menu item for scan function
    for step in Steps.values():
        step_function_item = FunctionItem(step.name,timeDo,[step])
        step_menu.append_item(step_function_item)

    # Get each Task, make a menu item for scan function
    for task in Tasks.values():
        task_function_item = FunctionItem(task.name,task.do)
        task_menu.append_item(task_function_item)

    # Get each Routine, make a menu item for scan function
    for routine in Routines.values():
        routine_function_item = FunctionItem(routine.name,routine.do)
        routine_menu.append_item(routine_function_item)

    # Create submenu items
    waypoint_submenu_item = SubmenuItem("Waypoints",waypoint_menu,main_menu) 
    step_submenu_item = SubmenuItem("Steps",step_menu,main_menu) 
    task_submenu_item = SubmenuItem("Tasks",task_menu,main_menu)
    routine_submenu_item = SubmenuItem("Routines",routine_menu,main_menu)

    # Append submenus to menu
    main_menu.append_item(waypoint_submenu_item)
    main_menu.append_item(step_submenu_item)
    main_menu.append_item(task_submenu_item)
    main_menu.append_item(routine_submenu_item)

    # Show menu
    main_menu.show()            
            
if __name__ == "__main__":
    main()