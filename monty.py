"""To run, type python monty.py

Even for the small number of 100 runs, for almost every run you will see
that the number of successes for switching is on the order of 2x that for
not switching.
"""
import copy
import random

def play(switch):
    doors = ['car','goat','goat']
    random.shuffle(doors) # we now don't know where the car is
    door_numbers = [0,1,2] # doors are numbered 0,1,2
    contestant_selection = random.choice(door_numbers)
    del door_numbers[contestant_selection]
    # door_numbers are now the numbers of the 2 doors monty can select.
    # We are now interested in the door monty does not select, which
    # is the car if it is behind the remaining doors. Otherwise
    # it is a random selection of the 2 remaining doors
    if doors[door_numbers[0]] == 'car':
        monty = door_numbers[1]
        not_monty = door_numbers[0]
    elif doors[door_numbers[1]] == 'car':
        monty = door_numbers[0]
        not_monty = door_numbers[1]
    else:
        monty = random.choice(door_numbers)
        not_monty = door_numbers[abs(1-monty)]
    # the car must be either behind contestant_selection or not_monty
    print 'Contestant selects:', contestant_selection
    print 'Monty shows a goat behind:', monty
    print doors[monty] 
    if switch:
        final_selection = not_monty
        print 'Contestant switches to door #', final_selection
    else:
        final_selection = contestant_selection
        print 'Contestant stays with door #', final_selection
    if doors[final_selection] == 'car':
        print 'Yay! Contestant wins a shiny new car.'
        return True
    else:
        print 'Bahhhh!'
        return False

def sim(iterations, switch):
    count = 0
    for i in range(0,iterations):
        if play(switch):
            count += 1
    return count

if __name__=="__main__":
    ITERATIONS = 100
    switch = sim(ITERATIONS, True)
    noswitch = sim(ITERATIONS, False)
    print
    print 'Switch:', switch
    print 'Noswitch:', noswitch

