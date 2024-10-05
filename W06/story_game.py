# importing libraries to create functions for a "typewriter" text effect

import sys, time

# creating functions for delayed text printing and input

def delprint (text):
    for character in text:
        sys.stdout.write (character)
        sys.stdout.flush ()
        time.sleep (0.05)

def delinput (text):
    for character in text:
        sys.stdout.write (character)
        sys.stdout.flush ()
        time.sleep (0.05)
    value = input ()
    return value    

delprint ("You find yourself stranded in an unfamiliar area inside a foggy forest.\n")
print ()
time.sleep (1)

delprint ("It's late at night, so the forest is wrapped in darkness.\n")
print ()
time.sleep (1)

light_source = delinput ("You stumble across a MATCHBOX and a FLASHLIGHT. Which one do you pick up? ")
print ()

# choice: matchbox

if light_source.lower() == "matchbox":
    delprint ("Despite the ground around you being pretty soggy, the matchbox and the matches inside were dry enough to work.\n")
    print ()
    time.sleep (1)

    delprint ("You decided to make a torch out of your undershirt and the hand sanitizer you had in your pocket.\n")
    print ()
    time.sleep (1)

    delprint ("The torch was bright enough to light up your path.\n")
    print ()
    time.sleep (1)

    delprint ("After walking for a bit, you find yourself on a crossroad.\n")
    print ()

    turn = delinput ("To the RIGHT is a winding path, and to the LEFT is a narrow path. Where do you turn? ")
    print ()

    # choice: right

    if turn.lower() == "right":
        delprint ("You choose to follow the path to your right and end up in a strange camp.\n")
        print ()
        time.sleep (1)

        delprint ("There, you're greeted by a group of people who appear to be startled. They seem disturbed by your presence.\n")
        print ()
        time.sleep (1)

        torch_choice = delinput ("Maybe your torch is scaring them? Will you PUT IT OUT or KEEP MOVING? ")
        print ()

        # choice: put it out

        if torch_choice.lower() == "put it out":
            delprint ("You put out the torch and set it on the ground in hopes that the strange people will stop being scared of you and tell you how to get out of the forest.\n")
            print ()
            time.sleep (1)

            delprint ("But now that you think about it, they don't look too human...\n")
            print ()
            time.sleep (0.4)

            delprint ("'NO!!'\n")
            print ()
            time.sleep (1)

            delprint ("You screamed in utter despair as the creatures leapt your way.\n")
            print ()
            time.sleep (0.5)

            delprint ("This is the end of the road for you, wanderer.\n")
            print ()
            time.sleep (0.5)

            delprint ("Thank you for playing!")

            # choice: keep moving

        elif torch_choice.lower() == "keep moving":
            delprint ("As you got closer to the strange people, you began to feel more uneasy.\n")
            print ()
            time.sleep (1)

            delprint ("You could swear you heard an unnatural hissing sound when you passed by one of them. This noise sent shivers down your spine, so you hurriedly left the area.\n")
            print ()
            time.sleep (1)

            delprint ("There were less and less trees as you kept moving forward, and in just about 10 minutes you found yourself in the outskirts of the city.\n")
            print ()
            time.sleep (1)

            delprint ("'Just what in the world were those creatures?' You had a brief thought to yourself.\n")
            print ()
            time.sleep (0.5)

            delprint ("This is the end of the road for you, wanderer.\n")
            print ()
            time.sleep(0.5)

            delprint ("Thank you for playing!")
            
        else:
            delprint ("Invalid choice!")

            # choice: left

    elif turn.lower() == "left":
        delprint ("You chose to follow the path to your left, and after some time find an abandoned cabin in the woods.\n")
        print ()
        time.sleep (1)

        cabin_choice = delinput ("It looks uninhabited, so there probably isn't anyone living inside. Will you ENTER it or LEAVE it be? ")
        print ()

        # choice: enter

        if cabin_choice.lower() == "enter":
            delprint ("You decided to come inside because you were getting pretty cold without your undershirt.\n")
            print ()
            time.sleep (1)

            delprint ("The door was open, so you were able to enter easily.\n")
            print ()
            time.sleep (1)

            delprint ("As soon as you closed the door behind you, a strange screeching noise could be heard from outside. You thought it might've just been the wind.\n")
            print ()
            time.sleep (1)

            delprint ("After exploring the house for a bit, you found a fireplace and dry wooden logs, so you made a fire with the matches you picked up earlier.\n")
            print ()
            time.sleep (1)

            delprint ("You warmed up and soon hit the road again.\n")
            print ()
            time.sleep (1)

            delprint ("It wasn't very long before you found the exit from the forest, safe and sound.\n")
            print ()
            time.sleep (0.5)

            delprint ("This is the end of the road for you, wanderer.\n")
            print ()
            time.sleep (0.5)

            delprint ("Thank you for playing!")

            # choice: leave

        elif cabin_choice.lower() == "leave":
            delprint ("You decided that it would be best to keep moving, even though you were getting pretty cold without your undershirt.\n")
            print ()
            time.sleep (1)

            delprint ("Not even a few minutes later, you heard an ear-spliiting screech.\n")
            print ()
            time.sleep (1)

            delprint ("You jumped and froze in place, shocked and alerted by the sudden sound. It accidentally made you drop your torch, so it went out because of the wet ground.\n")
            print ()
            time.sleep (1)

            delprint ("It only took you a second to feel a cold breath on your neck.\n")
            print ()
            time.sleep (0.4)

            delprint ("'What-'\n")
            print ()
            time.sleep (1)

            delprint ("The creature didn't let you finish.\n")
            print ()
            time.sleep (0.5)

            delprint ("This is the end of the road for you, wanderer.\n")
            print ()
            time.sleep (0.5)

            delprint ("Thank you for playing!")
            
        else:
            delprint ("Invalid choice!")
            
    else:
        delprint ("Invalid choice!")

# choice: flashlight

elif light_source.lower() == "flashlight":
    delprint ("To your surprise, the flashlight is still in working order.\n")
    print ()
    time.sleep (1)

    delprint ("After turning the flashlight on, you see a path that leads forward, hopefully out of the forest.\n")
    print ()
    time.sleep (1)

    delprint ("As you keep walking, the battery dies, but the only choice you have is to keep moving forward.\n")
    print ()
    time.sleep (1)

    noise_choice = delinput ("Suddenly, you hear a weird whistling growl and a rustle of the leaves. Do you CHECK what it is, RUN, or STAY STILL? ")
    print ()

    # choice: check

    if noise_choice.lower() == "check":
        delprint ("You decide to follow the noise and go deeper inside the bushes.\n")
        print ()
        time.sleep (1)

        delprint ("It's terribly dark and you're starting to think that this was a bad idea.\n")
        print ()
        time.sleep (1)

        delprint ("It was.\n")
        print ()
        time.sleep (1)

        delprint ("The growling stopped, and a moment later you felt a sharp pain in your back.\n")
        print ()
        time.sleep (1)

        delprint ("Your vision went pitch-black.\n")
        print ()
        time.sleep (0.5)

        delprint ("This is the end of the road for you, wanderer.\n")
        print ()
        time.sleep (0.5)

        delprint ("Thank you for playing!")

        # choice: run

    elif noise_choice.lower() == "run":
        delprint ("You thought that the best option of survival you have is to get out as soon as possible.\n")
        print ()
        time.sleep (1)

        delprint ("You begin running in the opposite direction from the noise, completely driven by panic and fear.\n")
        print ()
        time.sleep (1)

        delprint ("Something trips you up and you fall face-first into a muddy swamp.\n")
        print ()
        time.sleep (1)

        delprint ("As you tried to get up and keep running, the whistling growl caught up with you.\n")
        print ()
        time.sleep (0.5)

        delprint ("This is the end of the road for you, wanderer.\n")
        print ()
        time.sleep (0.5)

        delprint ("Thank you for playing!")
        
        # choice: stay still
        
    elif noise_choice.lower() == "stay still":
        delprint ("You thought that maybe if you were to stay still for a while, the creature would eventually leave and you'd be safe.\n")
        print ()
        time.sleep (1)
        
        delprint ("You thought wrong.\n")
        print ()
        time.sleep (1)
        
        delprint ("As you stood there in silence, your anxiety started to worsen.\n")
        print ()
        time.sleep (1)
        
        delprint ("You began sweating profusely and your breath was becoming heavier with each unbearably long second.\n")
        print ()
        time.sleep (1)
        
        delprint ("Something about the air around you felt off...\n")
        print ()
        time.sleep (1)
        
        delprint ("It could smell your fear.\n")
        print ()
        time.sleep (1)
        
        delprint ("Your last moment was painted crimson. The blinding moon was glaring at you through the trees.\n")
        print ()
        time.sleep (0.5)
        
        delprint ("This is the end of the road for you, wanderer.\n")
        print ()
        time.sleep (0.5)
        
        delprint ("Thank you for playing!")
        
    else:
        delprint ("Invalid choice!")

else:
    delprint ("Invalid choice!")
