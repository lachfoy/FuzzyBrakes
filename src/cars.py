# Written by Norbert Pop

import random as rng

class LeadCar:
    def __init__(self):
        self.speed = min(rng.randint(1, 90), 90) #Lead car can only go a maximum possible speed of 90
        self.pos = rng.randint(1, 1000) #Lead car will be starting somewhere randomly from 1 to 1000

    def updatePos(self):
        self.pos += self.speed

    def printStatus(self):
        print("Lead car speed: " + str(self.speed))
        print("Lead car position: " + str(self.pos) + "\n")

class TargetCar:
    def __init__(self, leadCar: LeadCar):
        self.speed = min(rng.randint(1, 60), 130) #Target car can only go a maximum possible speed of 130 and the fastest it can start at is 60
        self.leadCar = leadCar #Get a reference to the car in front
        self.pos = rng.randint(0, leadCar.pos - 1) #Lead car will be starting somewhere randomly BEHIND the car in front
        self.posFromLead = (self.leadCar.pos - self.pos)

    def updateSpeed(self, brakeStrength):
        if brakeStrength != 0:
            self.speed -= max(round((brakeStrength / 4), 2), 0) #Car cannot go below 0 in speed
        else:
            self.speed += 1

    def updatePos(self):
        self.pos += self.speed
        self.posFromLead = (self.leadCar.pos - self.pos)

    def printStatus(self):
        print("Target car speed: " + str(self.speed))
        print("Target car position: " + str(self.pos))
        print("Target car distance from lead car: " + str(self.posFromLead) + "\n")