package com.example.mykotlinapp

/*
This class is the basic component of the program

It contains metadata and a Waypoint object
*Steps* -> Tasks -> Routines

<ins>Steps</ins>

Steps are Components that have a Waypoint attribute. They correspond to a specific action that a user will take to progress their activity. Steps have a Waypoint associated to a guide the user to a location and check that they went. Steps have a many to one relationship with Tasks.

- Step Name
- Step Description
- Waypoint
 */

class Step(_name: String, _description: String, _waypoint: Waypoint): Component(_name,_description) {
    var waypoint: Waypoint = _waypoint

    override fun toString(): String {
        var string = super.toString()
        var waypointString = this.waypoint.toString()
        return string + " | Waypoint: " + waypointString
    }

    override fun action(): String {
        var string = this.waypoint.action()
        return "step action placeholder"
    }
}

/*fun main() {
    val waypoint = Waypoint("Test", "Test Description")
    val step = Step("Test", "Test Step Description", waypoint)
    println(step.toString())
}*/