import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from format_date import format_date
from stretch_packages import inflexbile as inflx, challenging_stretch as chln, advanced_stretch as advstr


def print_stretches(stretches):
    for stretch in stretches:
        print(stretch)
    print("Hold each pose for 30 seconds")
    

def gentle_stretching():
    stretches = []
    for i in range(1, 4):
        current_stretch = inflx.gentle_stretch()
        while current_stretch in stretches:
            current_stretch = inflx.gentle_stretch()
        stretches.append(current_stretch)
    print_stretches(stretches)


def challenging():
    stretches = []
    for i in range(1, 4):
        current_stretch = chln.intermediate_stretches()
        while current_stretch in stretches:
            current_stretch = chln.intermediate_stretches()
        stretches.append(current_stretch)
    print_stretches(stretches)


def advanced():
    stretches = []
    for i in range(1, 4):
        current_stretch = advstr.advanced_stretch()
        while current_stretch in stretches:
            current_stretch = advstr.advanced_stretch()
        stretches.append(current_stretch)
    print_stretches(stretches)

def choice():
    date = format_date()
    print(f"Welcome to the stretching session of {date}")
    print("Do you want this stretching to be (1) Gentle, (2) Challenging, (3) Intense?")
    choice = 0
    while choice not in [1, 2, 3]:
        try:
            choice = int(input())
            if choice not in [1, 2, 3]:
                print("Please select one of the following options: ")
                print("1. Gentle")
                print("2. Challenging")
                print("3. Intense")
                choice = int(input())
            else:
                break
        except ValueError:
            print("Please Enter an integer as your selection")
    
    if choice == 1:
        gentle_stretching()
    elif choice == 2:
        challenging()
    elif choice == 3:
        advanced()
    