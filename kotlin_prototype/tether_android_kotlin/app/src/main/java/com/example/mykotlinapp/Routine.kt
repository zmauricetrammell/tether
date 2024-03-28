package com.example.mykotlinapp

/*
Routines

Routines are Components that hold groups of Tasks. Routines correspond to an ordered set of tasks. Routines, once started, will prompt the user to complete Tasks, Step by Step.

- Routine Name
- Routine Description
- Task List
*/

class Routine(_name: String, _description: String, _taskList: List<Task>): Component(_name,_description) {
    var taskList: List<Task> = _taskList

    override fun toString(): String {
        var string = super.toString()
        var taskListString = StringBuilder()
        for (task in taskList) {
            taskListString.append(" ")
            taskListString.append(task.toString())
        }
        return string + taskListString.toString()
    }

    override fun action(): String {
        for (task in this.taskList) {
            var string = task.action()
        }
        return "routine action placeholder"
    }
}
