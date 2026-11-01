import time
print("Welcome to Study Reminder Agent!")
name = input("Enter your name: ")

print("Hello", name)
print("Let's start studying!")
subject = input("Which subject do you want to study? ")

print("Your selected subject is:", subject)
duration = input("How many minutes do you want to study? ")

print("Your study time is:", duration, "minutes")
print("Your study session is ready!")
print("Stay focused and do your best!")
print("Your reminder timer is starting...")
minutes = int(duration)
time.sleep(minutes*60)
print("Time is up!")
print("Great job, Amna! Take a short break.")