# Q1) Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the numbers
from threading import Timer
timeout = 10.00
t = Timer(timeout, print, ['Sorry, times up'])
t.start()

input_number = int(input("Enter a number: "))
t.cancel()

completed_list = []

while timeout == False:
    completed_list.append(input_number)
    if timeout == True:
        break

completed_list.append(input_number)
print(completed_list)
print(sum(completed_list))