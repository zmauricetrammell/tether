from component import Component
from waypoint import Waypoint

Steps = {}

""" 
This class is the basic component of the program

It contains metadata and a Waypoint object
*Steps* -> Tasks -> Routines

<ins>Steps</ins>

Steps are Components that have a Waypoint attribute. They correspond to a specific action that a user will take to progress their activity. Steps have a Waypoint associated to a guide the user to a location and check that they went. Steps have a many to one relationship with Tasks.

- Step Name
- Step Description
- Waypoint

"""

class Step(Component):
    def __init__(self, name, description,waypoint: Waypoint):
        super().__init__(name, description)
        self.waypoint = waypoint

    def toString(self):
        return("Name: {} | Description: {} | Waypoint: ({})".format(self.name,self.description,self.waypoint.toString()))
    
    def do(self):
        print(self.toString())
        print()
        self.waypoint.scan()
 
def main(): 
    #testStep = createStep()
    waypoint_a = Waypoint("Waypoint A","Waypoint in Place","Place","00000")
    test_step = Step("Step A","Description of Step A",waypoint_a)
    print(test_step.toString())
    
   
# __name__ 
if __name__=="__main__": 
    main()