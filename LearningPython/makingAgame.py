from time import sleep
weapon = False

def SkeletonFight():
  actions = ["fight","flee"]
  global weapon
  print("The three skeletons have noticed you! They seem ready for a fight!. You can either run or flee. What would you like to do?")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight")
    userInput = input()
    if userInput == "fight":
      if weapon:
        print("You kill the goul with the knife you found earlier. After moving forward, you find one of the exits. Congats!")
        quit()
      else:
        print("They will never find your body...")
      quit()
    elif userInput == "flee":
      showSkeletons()
    else:
      print("Please enter a valid option.")
      
def showSkeletons():
  directions = ["backward","forward"]
  global weapon
  print("You see a group of 3 skeletons on the far side of the room. What would you like to do?")
  userInput = ""
  while userInput not in directions:
    print("Options: Look around/left/backward/forward")
    userInput = input()
    if userInput == "left":
      if weapon:
        print("the hole has closed up, the more you look at the walls, the more they seem to be alive. Every now and then... the closed oraface twitches...")
      else:
        print("You reach your hand deep into the hole. It is wet...")
        sleep(2)
        print("The walls of the hole seem to wriggle and churn... you think you might vomit...")
        sleep(2)
        print("finally your fingers grasp something, you pull your hand out and find it covered in blood and filth... in your hand you see a gleaming, razor sharp dagger.")
      weapon = True
    elif userInput == "backward":
      introScene()
    elif userInput == "forward":
      SkeletonFight()
    elif userInput == "look around":
      if weapon:
        print("directly in front of you is a small group of skeletons, they are unarmored, and unarmed, yet they still look dangerous. You feel confident you can take them.")
        sleep(.5)
        print("To your left, the hole you found the dagger in has closed up, occasionally it twitches...")
        sleep(.5)
        print("behind you is the room you came from... it is never too late to back away.")
      else:
        print("directly in front of you is a small group of skeletons, they are unarmored, and unarmed, yet they still look dangerous. If you had a weapon, you might stand a chance.")
        sleep(.5)
        print("To your left you see a small hole in the wall, just big enough for you to fit your arm through.")
        sleep(.5)
        print("Behind you, the hall leads to the room you came from.")
      showSkeletons()
    else:
      print("Please enter a valid option.")
      

def hauntedRoom():
  directions = ["right","left","backward"]
  print("You hear wailing, crying and screams... the air chills to the point of freezing. Your breath is now vapor before your eyes and your lantern flickers and dims")
  userInput = ""
  while userInput not in directions:
    print("Options: Look around/Right/Left/Backward")
    userInput = input()
    if userInput == "right":
      print("You go down the hallway to the right, even though your very bones are raging against you... A spectre lunges out at you, and consumes your very soul... You die!")
      quit()
    elif userInput == "left":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "backward":
      introScene()
    elif userInput == "look around":
      print("Looking around, you notice the walls are covered in frost, and the ground cracks and breaks under your feet. There is the sound of wailing and screaming that carries in the air.")
      sleep(2)
      print("To your right, you can more clearly hear the screams, and you can tell the air gets colder. You feel a deep sense of dread...")
      sleep(2)
      print("To the left, you can see a light, perhaps this is the exit?!")
    else:
      print("Please enter a valid option.")

def ExitScene():
  directions = ["forward","backward"]
  print("You can see a bright light shining from the end of this hallway! You are at the exit!")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "backward":
      SlimeFight()
    else:
      print("Please enter a valid option.")
      
def SlimeFight():
  directions = ["right","backward"]
  global weapon
  print("You see a large slime in the center of the room. You are creeped out. What would you like to do?")
  userInput = ""
  while userInput not in directions:
    print("Options: Look around/Right/Backward/Fight")
    userInput = input()
    if userInput == "right":
      ExitScene()
    elif userInput == "backward":
      introScene()
    elif userInput == "look around":
      print("The large black slime in the center of the room is easily ten feet wide, you can see bones, hair and steel all poking out of it at odd angles. This thing is dangerous...")
      sleep(1)
      print("There is only one way to progress, the cave continues to the right.")
    elif userInput == "fight":
      if weapon:
        print("You decide to fight the black slime...")
        sleep(1)
        print("You lunge forward and drive your dagger deep into the slime! You draw back your blade and prepare to attack again!")
        sleep(1)
        print("Your drive the dagger back into the slime, but this time your blade gets stuck! As you struggle, your legs get covered in the slime and you slowly get digested!")
        sleep(2)
        print("You die!")
        quit()
      else:
        print("you decide to attack the slime with your bare hands!")
        sleep(2)
        print("That was a terrible idea... You die!")
        quit()
    else:
      print("Please enter a valid option.")


def introScene():
  directions = ["look around","left","right","forward"]
  print("You are at a crossroads. What would you like to do?")
  userInput = ""
  while userInput not in directions:
    print("Options: Look around/left/right/backward/forward")
    userInput = input()
    if userInput == "left":
      SlimeFight()
    elif userInput == "right":
      showSkeletons()
    elif userInput == "forward":
      hauntedRoom()
    elif userInput == "backward":
      print("You find that the hallway you just came from is now a solid wall!")
    elif userInput == "look around":
      print("Your lantern casts twisted shadows upon the walls that trick your eyes and mind... Your own shadow climbs the wall behind you, as if preparing to consume you. you hear something...")
      sleep(2)
      print("You hear shuffling and creaking noises echo down the hall to the right")
      sleep(2)
      print("You hear a wet, slurping, sloppy sound come from the hall to the left")
      sleep(2)
      print("You hear a soft, faint wailing sound cry out from directly ahead of you.")
      sleep(.5)
      introScene()
    else: 
      print("Please enter a valid option.")

if __name__ == "__main__":
  while True:
    print("Welcome to the Adventure Game!")
    sleep(1)
    print("You are an adventurer who decided to explore a cave")
    sleep(1)
    print("However, during your exploration, you find yourself lost!")
    sleep(1)
    print("You got turned around and have no clue how to escape, all you can do is explore and find an exit")
    sleep(1)
    introScene()