**Tether**

Executive disfunction assistive program designed to record and manage the execution of routines.

**Motivation:**

Many neurodivergent patterns like ADHD or Autism exhibit executive disfunction, which disrupts a person's ability to manage their own thoughts, emotions, and actions. This leaves many people struggling to complete basic routines and tasks like washing the dishes, taking out the trash, brushing their teeth. For these routine tasks, the order matters and the motivation to start is critical to the execution. 

This project is an attempt at outsourcing the executive function to an assistive tool that will guide the user through a predefined routine to overcome distraction, confusion, and low motivation.

**Concept:**

This project allows users to use RFID tag "beacons" to designate physical locations that correspond to tasks. Then the user will record sequences of tasks and specific actions to create routines. The user interface will guide the user through the desired routine by prompting the user to scan each of the beacons corresponding to the recorded actions, preventing distraction or confusion and enforcing completion.

**General Functionality:**

<ins>Make a Beacon</ins>
Users are prompted to create a beacon by inputting its attributes and scanning the RFID tag to save the code.

Example:
Create a Beacon, Kitchen Sink, associated with an RFID tag stuck near your kitchen sink.

<ins>Make an Action</ins>
Users are prompted to create a saved action by inputting its attributes and selecting a location beacon from the saved list or creating a new one from scratch.

Example: 
Create an Action, Wash Dishes, associated with the kitchen sink beacon.

<ins>Make a Task</ins>
Users are prompted to create a saved task by inputting its attributes then selecting and ordering actions that fit within or creating actions from scratch.
- Tasks have shirt sizes: small, medium, and large corresponding to how many times the user needs to scan the tag over a period of time (combat distractions)
  
Example:
Create a Task, Do Dishes, comprised of: Go to Kitchen Sink, Wash Dishes (Start), Wash Dishes (Poke), Wash Dishes (Finish)


<ins>Make a Routine</ins>
Users are prompted to add and sequence tasks from application memory or create a new task from scratch.
- Tasks should be shown in a list to be added

Example:
Create a Routine by joining Do Dishes, Clean Counters, and Mop Floor.


**Areas of Focus:**

- Python (Rapid Protyping)
- Tkinter (GUI Prototyping)
- Android Studio / Java (Android App)
- RFID / NFC Technology
