#Isaiah Schafer
#Case Study_if_else_while
#The purpose of this is to check if a students GPA
#meats requirments for the Honor Roll or Deans List.

last_name: str = input("Please enter your last name (Enter ZZZ to quit): ")
first_name: str = input("Please enter your first name: ")

gpa: float = input("Please enter your GPA: ")

while last_name != "ZZZ":
    if gpa >= 3.5:
        print("You have made the deans list.")
    elif gpa >= 3.25:
        print("You have made the Honor Roll.")
    last_name: str = input("Please enter your last name (Enter ZZZ to quit)")