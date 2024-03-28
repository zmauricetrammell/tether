package com.example.mykotlinapp

/*
Components

Components are a shell parent class that have metadata fields.

- Component Name
- Component Description
 */

abstract class Component(_name: String, _description: String){
    var name: String
    var description: String

    init {
        this.name = _name
        this.description = _description
    }

    // Override the toString() method to return a string of relevant data
    override fun toString(): String {
        var string: String = "Name: " + this.name + " | Description: " + this.description
        return string
    }

    abstract fun action():String

}