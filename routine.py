from component import Component
from waypoint import Waypoint
from step import Step
from task import Task

"""
Routines

Routines are Components that hold groups of Tasks. Routines correspond to an ordered set of tasks. Routines, once started, will prompt the user to complete Tasks, Step by Step. 

- Routine Name
- Routine Description
- Task List
"""

class Routine(Component):
    def __init__(self, name, description, tasks: list):
        super().__init__(name, description)
        self.tasks = tasks

    def toString(self):
        return("Name: {} | Desciption: {} | Tasks: ({})".format(self.name,self.description, [task.toString() for task in self.tasks]))
    
    def do(self):
        print(self.toString())
        print()
        for task in self.tasks:
            task.do()
        
def main():
    kitchen_waypoint = Waypoint("Kitchen","Waypoint in kitchen","Kitchen Sink")
    go_to_kitchen_step = Step("Go: {}".format(kitchen_waypoint.name),"Go to Kitchen",kitchen_waypoint)
    do_dishes_step = Step("Dishes","Clean Dishes",kitchen_waypoint)
    clean_dishes_task = Task("{}".format(do_dishes_step.description), "Clean and put away the dishes", [go_to_kitchen_step,do_dishes_step])

    trash_waypoint = Waypoint("Trash","Waypoint at trash","Trash Can")
    door_waypoint = Waypoint("Front Door","Waypoint at Front Door","Front Door")
    go_to_trash_step = Step("Go: {}".format(trash_waypoint.name),"Go to Trash Can",trash_waypoint)
    get_trash_step = Step("Take Out Trash","Get Trash",trash_waypoint)
    go_to_door_step = Step("Go: {}".format(door_waypoint.name), "Go to Front Door",door_waypoint)
    take_out_trash_task = Task("Take Out Trash", "Take trash outside to dumpster", [go_to_trash_step,get_trash_step,go_to_door_step])

    night_routine = Routine("Night Routine", "Routine conducted nightly", [clean_dishes_task,take_out_trash_task])
    print(night_routine.toString())


if __name__=="__main__": 
    main()