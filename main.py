#author: Richard Rosenthal
#date 11-21-2020
#Ascii art by jgs on ascii.co.uk 
print('''
****************************************************************
                    .--.****************************************
    {\             / q {\***************************************
    { `\           \ (-(~`**************************************
   { '.{`\          \ \ )***************************************
   {'-{ ' \  .-""'-. \ \****************************************
   {._{'.' \/       '.) \***************************************
   {_.{.   {`            |**************************************
   {._{ ' {   ;'-=-.     |**************************************
    {-.{.' {  ';-=-.`    /**************************************
     {._.{.;    '-=-   .'***************************************
      {_.-' `'.__  _,-'*****************************************
         jgs   |||`*********************************************
              .='==,********************************************
****************************************************************
****************************************************************
''')
print("")

score = 0

print("Hello Turkey C-137. You are scheduled to be terminated and prepared for Thanksgiving night dinner")
print("However, it looks like this might be your lucky day.")
print("Whilst 2020 has been a horrible year for humans it might end up being your salvation")
print("While waiting for your inevitable end you notice that one of the farm hands left the barn door slightly ajar.")
print("")

choice_one = input("Do you inspect or stay put? (Enter 'inspect' or 'stay put')").lower()

if choice_one == 'inspect':
  print("")
  print("You hear dogs barking nearby")
  print("But it looks like one of the farmers has left the door open to their house")
  print("You decide to inspect further")
  choice_two = input("Should you run or walk? (Enter 'run' or 'walk')").lower()
  print("")

  score += 1
  if choice_two == 'run':
    print("")
    print("As you walk inside of the house you are presented with three different options")
    print("Yikes!!")
    print("There are three rooms, one in front of you at the end of a long hallway, one to your left and finally a door open to your right")
    print("Which room will you choose")
    choice_three = input("(Enter 'left', 'right,' or ahead)").lower()
    print("")
    score += 1
    if choice_three == 'right':
      print("")
      print("You entered the one on the right.")
      print("Good choice C-137")
      print("You can see the entrance and lucky for you the door is open")
      choice_four = input("Should you run or walk? (Enter 'run' or 'walk'").lower()
      print("")
      score += 1
      if choice_four == 'walk':
        print("")
        print("Good choice! Unbeknownst to you there was a cat sound asleep.")
        print("If you had ran you would have surely woken up Fluffy")
        print("You made it outside, you're almost free")
        print("You can see the road infornt of you and beyond it the woods")
        print("All you have to do is make it to the other side")
        print("Unfortunately the street is quite busy.")
        choice_five = input("Should you try to make a run for it or wait till traffic slows down?(Enter 'run' or 'wait')").lower()
        print("")
        score += 1
        if choice_five == 'run':
          print("")
          print("Horray! You made it across the road")
          print("You are free to live you life now as a wild turkey")
          print("However you have an overwhelming sense of guilt leaving your fellow birds behind")
          choice_six = input("Should you go back and rescue them or march foward to begin you new life? (Enter 'forward' or 'back')").lower()
          print("")
          score += 1
          if choice_six == 'forward':
            print("")
            print("That was a wise choice. While sad for the others, you")
            print("had to look out for yourself. Plus you were really lucky crossing the road the first time.")
            print("Congratulations! You won!")
            print("")
          else:
            print("")
            print("You should have gone foward")
            print("While it's great you chose the moral high road..")
            print("..you ended up roadkill on the actual road")
            print("Game Over")
            print("")

        else:
          print("")
          print("By waiting you allowed the farmer that saw you escape catch up to you")
          print("Out of spite, the farmer made you their dinner")
          print("Happy Thanksgiving?")
          print("Game Over")

      else:
        print("")
        print("By running you have awoken the cat who had been sound asleep")
        print("You try to outrun Fluffy but to no avail")
        print("Looks like you are cat food")
        print("Game Over")
    elif choice_three == 'left':
      print("")
      print("You walked right into the kitchen where you are met with the farmer cleaning his knife")
      print("Looks like your escape has come to an end")
      print("")
    else:
      print("")
      print ("Before you could make it down the hallway two dogs rush into the house")
      print("You just became a snack for fido.")
      print("Game Over")
      print("")

  else:
    print("")
    print("Oh no, you should have ran. One of the dogs intercepted you before you could get into the house...")
    print("Game Over")


else:
  print("")
  print ("Game over")

print("Thank you for playing!")
print("Your score was " + str(score))
print("Happy Thanksgiving")
print("")
