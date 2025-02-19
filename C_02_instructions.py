 # funtions go here

def yes_no(question):

    # Checks user response to a question is yes / no ***

    while True:

        response = input(question).lower()

        #check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "no":
           return "no"
        else:
            print("please enter yes / no")

def instructions():
    """Prints instructions"""

    print("""
*** Instructions ****

Roll the dice and try and win!
    """)

# Main routine

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("do you want instruction")

# Display the instructions if the user want to see them...
if want_instructions == "yes":
    instructions()

print ()
print("Program continues")
