import random

def stimulation_pi(numberPoints):
    insideCircle = 0
    for _ in range(numberPoints):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        #check if the points lies inside the circle
        if x**2+y**2 <= 1:
            insideCircle += 1
    
    #estimating the value of pi
    piEstimate = 4*insideCircle/numberPoints
    return piEstimate

numberStimulations = 100000
piEstimate = stimulation_pi(numberStimulations)
print(f"estimated value of pi with {numberStimulations} points is: {piEstimate}")