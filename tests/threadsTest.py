import threading
import time

# Status flag to stop the timer thread when inputs are received
flag = "GO"

# Reminder function
def reminder():
    while flag == "GO":
        count = 0
        while count < 5:
            if flag == "STOP":
                return
            time.sleep(1)
            count +=1
        print("Reminder")
        print(threading.active_count())


def getInput():
    text = input("Input: ")
    if text == "0":
        global flag
        flag = "STOP"


if __name__ == "__main__":
    timer_thread = threading.Thread(target = reminder)
    #input_thread = threading.Thread(target = getInput)
    timer_thread.start()
    #input_thread.start()
    getInput()

    