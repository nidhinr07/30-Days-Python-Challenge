# Day 17 - Time Module

import time


# Using time.time()
current_time = time.time()                    # Get current timestamp

print(current_time)                           # Display current timestamp


# Using time.ctime()
readable_time = time.ctime()                  # Get readable current time

print(readable_time)                          # Display current time


# Using time.sleep()
print("Start")                                # Display starting message

time.sleep(2)                                 # Pause program for two seconds

print("End")                                  # Display ending message


# Using sleep inside loop
for number in range(1, 4):

    print(number)                             # Display current number

    time.sleep(1)                             # Wait for one second
