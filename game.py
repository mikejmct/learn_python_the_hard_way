# python 2.7.3
# write an adventure game using all python tools you have used

from sys import exit
from sys import argv

script, username = argv
prompt = "> "

def crash(why):
    print why, "? ... you crashed, enjoy the hospital sucker."
    exit(0)

def win():
    print "What a race the fans love you!"
    print "You win the Le Mans!"
    print "CHAMPAGNE!"	
    exit(0)	

def lose():
    print "You need some practice."
    print "Someone throws an empty beer bottle at you."
    print "The wound is bleeding."
    raw_input(prompt)
    print "You look up through the blood and see it was your father."
    exit(0)

def second():
    print "Sergio does his best, but it's not good enough."
    print "You come second and look forward to next year."
    print "You look over to your family watching from the stand."
    raw_input(prompt)
    print "They look so proud."
    exit(0)	
	
def start_run():
    print "Hi %s you are racing in the Le Mans race." % (username)
    print "You have been training your whole life for this moment."
    print "You have a full crew, with extra drivers and in fourth position on the grid."
    print "The lights start the countdown."
    raw_input(prompt)
    print "RED"
    raw_input(prompt)
    print "ORANGE"
    raw_input(prompt)
    print "GREEN! GO! GO! GO!"
    raw_input(prompt)
    
    passing()
		
def passing():
    print "You need to pass people to get ahead."
    print "Do you take the inside line or the outside line?"
    pass_move = raw_input(prompt)  

    if "inside" in pass_move:
        crash(pass_move)

    elif "outside" in pass_move:
        print "Nice move you are almost in first place!"
        first_corner()

    else:
        print "That's not an option!"
        crash(pass_move)

def first_corner():
    print "You are side by side with the lead car."
    print "Do you think you can pass?"
    raw_input(prompt)
    brakeing()

def brakeing():
    brake = raw_input("Ok do you brake early or late? ")

    if "early" in brake:
        early_brake()
		
    elif "late" in brake:
        print "That's great you take the lead!"
        late_brake()
		
    else:
        print "Man you need to stay focused!"
    crash(brake)
    
def early_brake():
    print "Oh no that's not going to win the race!"
    raw_input(prompt)
    print "You are in last place for the next few hours."
    raw_input(prompt)
    print "It's time for a pitstop."
    driver_change_last()

def late_brake():
    print "That was a great passing manouver! The crowd goes wild!"
    print "You are out in front now."
    print "You lead the race for the next two hours."
    pitstop = raw_input("Your team wants to know if you want to take an early pitstop or wait? ")

    if "early" in pitstop:
        print "Lucky timing it started raining and you got wet tires at the stop!"
        driver_change_front()

    elif "wait" in pitstop:
        print "Oh no it rains and you still have dry tires on."
        print "You need to slow down for the next lap."
        raw_input(prompt)
        print "At the pitstop you fall back to last place!"
        driver_change_last()

    else:
        crash(pitstop)

def driver_change_last():
    print "You need a miracle! Pick your best replacement driver."
    print "You have Sally, Bobby John or Sergio on your team."
    driver = raw_input("Who's it gonna be? ")

    if "ally" in driver:
        sally()

    elif "obby" in driver:
        print "Oh no Bobby John is still drunk from last night."
        raw_input("Do you have any advice for him? \n")
        lose()

    elif "ergio" in driver:
        print "Good try but Sergio is not your best option."
        lose()

    else:
        crash(driver)

def driver_change_front():
    print "What a great first half of the race."
    print "Time for a driver change."
    print "You have Sally, Bobby John or Sergio on your team."
    driver = raw_input("Who's it gonna be? ")

    if "ally" in driver:
        print "This is your best chance Sally is four time Le Mans champ!"
        win()

    elif "obby" in driver:
        print "Oh no Bobby John is still drunk from last night."
        raw_input("Do you have any advice for him? \n")
        lose()

    elif "ergio" in driver:
        print "Good try but Sergio is not your best."
        second()

    else:
        crash(driver)

def sally():
    print "Sally is four time Le Mans champ."
    print "She is doing great but needs a pep talk."
    print "What do you say? "
    pep_talk = False

    while True:
        radio = raw_input(prompt)

        if radio == "Drive fast" and not pep_talk:
            lose("That is lame advice")

        elif radio == "You can do it" and not pep_talk:
            print "Sally thanks you and races harder!"
            win()

        elif radio == "I love you" and not pep_talk:
            print "Man you are so lame."
            print "Sally never talks to you again."
            lose()

        else:
            print "Time is running out!"

start_run()