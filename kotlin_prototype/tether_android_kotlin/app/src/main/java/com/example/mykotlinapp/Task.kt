package com.example.mykotlinapp

/*
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
 */

class Task(_name: String, _description: String, _stepList: List<Step>): Component(_name,_description) {
    var stepList: List<Step> = _stepList

    override fun toString(): String {
        var string = super.toString()
        var stepListString = StringBuilder()
        for (step in stepList) {
            stepListString.append(" ")
            stepListString.append(step.toString())
        }
        return string + stepListString.toString()
    }

    override fun action(): String {
        for (step in this.stepList) {
            var string = step.action()
        }
        return "task action placeholder"
    }
}
/*fun main() {
    val waypoint = Waypoint("Test Waypoint", "Test Waypoint Description")
    val step = Step("Test Step", "Test Step Description", waypoint)
    val stepList = listOf(step,step,step)
    val task = Task("Test Task", "Test Task Description", stepList)
    println(task.toString())
}*/