# Written by Lachlan Foy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create the required antecedents and consequents with their respective universes
speed = ctrl.Antecedent(np.arange(0, 131, 1), 'speed')
distance = ctrl.Antecedent(np.arange(0, 81, 1), 'distance')
brake = ctrl.Consequent(np.arange(0, 101, 1), 'brake pressure')

# Create the fuzzy sets and assign membership functions to ranges
speed['slow'] = fuzz.trimf(speed.universe, [0, 0, 65])
speed['medium'] = fuzz.trimf(speed.universe, [0, 65, 130])
speed['fast'] = fuzz.trimf(speed.universe, [65, 130, 130])
distance['close'] = fuzz.trimf(distance.universe, [0, 0, 40])
distance['medium'] = fuzz.trimf(distance.universe, [0, 40, 80])
distance['far'] = fuzz.trimf(distance.universe, [40, 80, 80])
brake['nil'] = fuzz.trimf(brake.universe, [0, 0, 0])
brake['soft'] = fuzz.trimf(brake.universe, [0, 0, 50])
brake['medium'] = fuzz.trimf(brake.universe, [0, 50, 100])
brake['hard'] = fuzz.trimf(brake.universe, [50, 100, 100])

# Implement the rule base and assign rules
rule1 = ctrl.Rule(speed['fast'] & distance['close'], brake['hard'])
rule2 = ctrl.Rule(speed['fast'] & distance['medium'], brake['medium'])
rule3 = ctrl.Rule(speed['fast'] & distance['far'], brake['soft'])
rule4 = ctrl.Rule(speed['medium'] & distance['close'], brake['medium'])
rule5 = ctrl.Rule(speed['medium'] & distance['medium'], brake['soft'])
rule6 = ctrl.Rule(speed['medium'] & distance['far'], brake['nil'])
rule7 = ctrl.Rule(speed['slow'] & distance['close'], brake['nil'])
rule8 = ctrl.Rule(speed['slow'] & distance['medium'], brake['nil'])
rule9 = ctrl.Rule(speed['slow'] & distance['far'], brake['nil'])
braking_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

# Create the control system simulation
braking = ctrl.ControlSystemSimulation(braking_ctrl)

# Function to compute the output using Mamdani Inference
def computeBraking(Speed, Distance):
    braking.input['speed'] = Speed
    braking.input['distance'] = Distance
    braking.compute()
    return braking.output['brake pressure']