# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:


        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item


        print(error)
        print()




# Display instructions
def instructions():
    print('''
    
**** Instructions ****

To begin, choose the number of rounds (or pick infinite mode).

Then play against the computer. You need to choose R (rock), P (paper) S (scissors)

The rules are as follows:
o Paper beats rock
o Rock beats scissors
o Scissors beats rock

Good Luck!
    ''')



# Main routine
print()
print("🪨📄✂️ Rock / Paper / Scissors Game 🪨📄✂️")
print()

# ask user if they want the instructions and display
# them if requested
want_instructions = string_checker("Do you want instructions? ")

# check user enters yes or no
if want_instructions == "yes":
    instructions()

print("program continues")