#import helper
from helper import validate_and_execute,user_input_message

# while loop - We need to use the user_input to initalize user inputs to the application
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_units = user_input.split(":")
    days_and_units_dictionary = {"days": days_and_units[0], "units":days_and_units[1]}
    validate_and_execute(days_and_units_dictionary)