import datetime

user_input = input("Enter your goal with a deadline, separated by :\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

# print(input_list)

converted_deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")
print(converted_deadline)
print(type(converted_deadline))

# calculation how many days from now till deadline

today_date = datetime.datetime.now()
print(today_date)
day_to_goal = converted_deadline - today_date

print(day_to_goal)