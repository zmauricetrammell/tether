package com.example.mykotlinapp

/*
Waypoints

This class is the location component of the program.

Waypoints correspond to a location in the user's environment, they have
standard component metadata and additional location and code attributes.
Waypoints are used to track where the larger action object will require
the user to be. Waypoints have RFID tags that will be scanned to initiate
and conclude actions.
 */
class Waypoint(_name: String, _description: String): Component(_name,_description) {
    var code: String = "00000"

    override fun toString(): String {
        var string = super.toString()
        return string + " | Code: " + this.code
    }

    // TODO: Needs to pull input from user
    override fun action(): String {
        var string = this.toString()
        return "waypoint action placeholder"
    }
}

/*fun main() {
    val waypoint = Waypoint("Test","Test D")
    println(waypoint.toString())
}*/