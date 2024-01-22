import random

# global variables
treasure = 0
health = 5
#turns = 0
torch = False
whip = True

# function to simulate 20 sided dice roll
def dice_roll():
    return random.randint(1, 20)

# function to search room once cleared of obstacles etc.
def search_room():
    roll = dice_roll()
    global torch
    global health
    global treasure


# function to move through passages connecting rooms
def enter_passage():
    global torch
    global health
    global whip
    roll = dice_roll()
    # There is a 50/50 chance of passage being darkened and with dangers or lit with torches
    if roll < 11:
        print("As you enter the darkened passageway you get a bad feeling.")
        roll = dice_roll()
        if(roll < 4):
            print("You can sense hundreds of small creatures writhing around you,")
            print("The passage is teaming with RATS!")
            if(torch):
                print("Fortunately you have a flaming torch, which you use to clear a path through to the next room")
            else:
                print("As you move through the passage some of the rats attack you.")
                print("You lose a health point.")
                health -= 1
        elif(roll < 8):
            print("You can hear rattling noises as you enter and can sense movement on the floor")
            print("There are SNAKES slithering in this passageway!")
            if(torch and whip):
                print("With the light of your torch you see a hook on the ceiling.")
                print("With your whip you are able to swing across the passageway to safety.")
            elif(torch):
                print("You throw the torch into the passage and the snakes slither away")
                print("Unfortunately you are unable to retrieve your torch")
                torch = False




    else:
        print("You enter a passageway with lighted torches on the wall.")
        if not torch:
            print("You take a torch from the wall. It might be useful.")
            torch = True
        print("You pass through to the next room with no incident.")


def check_game_state():
    pass

def room_1():
    print("You pass from the tomb entrance into a large dusty room.")
    print("There are pieces of broken statues and crumbling columns, ")
    print("there are passages leading out of the room to the east and south.")
    # put the following into a function?

def search_room():
    select = input("Do you want to search the room before moving, press s to search any key to move on?")
    if select == 's':
        pass




def room_2():
    pass

def room_3():
    pass

def room_4():
    pass

# initialise game
# loop while game running
# enter_room(current_room)
# check if room has been visited
#   if not already visited deal with room events  - check game situation
# prompt for search
#   do_search
#      deal with search events - check for game situation
# prompt for next direction
#   choose new direction (set next_room)
# move to next passage
#   deal with events in passage (pick up torch)
#   set next_room to current_room
# return to while loop
# (checking game situation can end while loop)

# once loop exited prompt for victory/ defeat
# prompt for new game

