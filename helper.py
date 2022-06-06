calculation_to_units = 24
name_of_units = "hours"

import helper


def days_to_units(number_of_days,units_conversion):
    if units_conversion == "hours":
        return f"{number_of_days} days are {number_of_days * 24} {units_conversion}"
    elif units_conversion == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} {units_conversion}"
    else:
        return "unsuported value"



def validate_and_execute(days_and_units_dictionary):
#    try: 
    user_input_int = int(days_and_units_dictionary["days"])   
    user_input_conversion= days_and_units_dictionary["units"]
    # if user_input_int.isdigit():
        ## we are casting the data into integer
        # user_input_int = int(num_of_days_element)   
    if user_input_int > 0:
        days_to_units(user_input_int,user_input_conversion)  
        calculated_value = days_to_units(user_input_int,user_input_conversion)
        print(calculated_value)
    elif user_input_int == 0:
        print ("you entered a 0 value, please enter a value greater then 0")

    else:
        print("your input is not a number, please enter an integer")

user_input_message = "Hello, enter the number of days and conversion!\n"
