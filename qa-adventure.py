import os

inventory = []

def clear():
    os.system("clear")

def pause():
    ready = raw_input("Enter to continue")

def your_cube():
    print("\nYou are sitting your in cube.  Your laptop is on your desk?")
    print("'o' - Open your laptop and test something.")
    print("'w' - Walk outside of your cube. \n")

    choice = raw_input("What do you want to do?: ")
    if choice == 'o':
        print("\nYou open your laptop, start testing and found a crash bug.")
        inventory.append("crash bug")
        your_cube()
    if choice == 'w':
        outside_cube()

def outside_cube():
    print("\nYou are standing outside of your cube.")
    print("'b' Walk back into your cube.\n")
    
    choice = raw_input("What do you want to do?: ")
    if choice == 'b':
        your_cube()

clear()
your_cube()




