**Tether**

Executive disfunction assistive program designed to record and manage the execution of routines.

**Motivation:**

Many neurodivergent patterns like ADHD or Autism exhibit executive disfunction, which disrupts a person's ability to manage their own thoughts, emotions, and actions. This leaves many people struggling to complete basic routines and tasks like washing the dishes, taking out the trash, brushing their teeth. For these routine tasks, the order matters and the motivation to start is critical to the execution. 

This project is an attempt at outsourcing the executive function to an assistive tool that will guide the user through a predefined routine to overcome distraction, confusion, and low motivation.

**Concept:**

This project allows users to use RFID tag "beacons" to designate physical locations that correspond to tasks. Then the user will record sequences of tasks and specific actions to create routines. The user interface will guide the user through the desired routine by prompting the user to scan each of the beacons corresponding to the recorded actions, preventing distraction or confusion and enforcing completion.

**General Functionality:**

<ins>Components</ins>

Components are a shell parent class that have metadata fields.

- Component Name
- Component Description

<ins>Waypoints</ins>

Waypoints are Components that have a location attribute and a code attribute. They correspond to an RFID tag and get the code from it to later check as the user scans waypoints to progress steps. Waypoints tell users where to go and allow the program to check that the user went there. Waypoints have a one to many relationship with Steps.

- Waypoint Name
- Waypoint Description
- Waypoint Location
- Waypoint Code

<ins>Steps</ins>

Steps are Components that have a Waypoint attribute. They correspond to a specific action that a user will take to progress their activity. Steps have a Waypoint associated to a guide the user to a location and check that they went. Steps have a many to one relationship with Tasks.

- Step Name
- Step Description
- Waypoint

<ins>Tasks</ins>

Tasks are Components that hold a group of Steps. Tasks have a priority attribute that allows the user to designate its relative importance compared to other tasks. Tasks correspond to a singe full activity: arrival at, execution of, and completion. Tasks have Steps associated with them to break them to chunks. Tasks, once started, require the user to check in by rescanning the Waypoint to show that they're still there. Tasks are completed by holding the scanner to the Waypoint for 5 seconds. Tasks share a many to many relationship with Routines. 

- Task Name
- Task Description
- Task Priority
- Steps List

<ins>Routines</ins>

Routines are Components that hold groups of Tasks. Routines correspond to an ordered set of tasks. Routines, once started, will prompt the user to complete Tasks, Step by Step. 

- Routine Name
- Routine Description
- Task List


**Areas of Focus:**

- Python (Rapid Protyping)
- Tkinter (GUI Prototyping)
- Android Studio / Java (Android App)
- RFID / NFC Technology
