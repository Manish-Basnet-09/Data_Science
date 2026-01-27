# File: main_program.py
import myutils

print("Running main_p.py")

message = myutils.greet("CSIT Student")
print(message)

sum_result = myutils.add_numbers(10, 25)
print(f"The sum is: {sum_result}")

print(f"Value of PI from myutils: {myutils.PI}")