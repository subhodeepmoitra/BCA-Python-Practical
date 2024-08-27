#Concept Recap:
#
#    You have 30 days to study for an exam.
#    The more days you study, the higher your chances of passing:
#        Study 20 or more days: 80% chance of passing.
#        Study 10 to 19 days: 50% chance of passing.
#        Study fewer than 10 days: 20% chance of passing.

import random

total_stimulations = int(input("enter the total stimulations: "))

days_in_month = 30

counter_for_passing = 0

current_stimulation = 0

while current_stimulation < total_stimulations:
    study_days = random.randint(0, days_in_month)

    # finding the possibility of pass
    if study_days > 20:
        pass_probability = 0.8
    elif 10 <= study_days <= 20:
        pass_probability = 0.5
    else:
        pass_probability = 0.2

    # stimulating whether pass or fail
    if random.random() < pass_probability:
        counter_for_passing += 1

    #increment the stimulation counter
    current_stimulation += 1

counting_passing_chance = (counter_for_passing / total_stimulations) * 100

print(f"Passing chances are: {counting_passing_chance:.2f}%")