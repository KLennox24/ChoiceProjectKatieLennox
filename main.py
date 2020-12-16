
explanation_check = input("Welcome to Fight or Flight! Have you played the game before? Type 'Y' if\nyes, 'N' if no.\n")

def game_explanation():
  print("\nIn this game, you will answer different scenarios you are presented with by answering either Fight or Flight. Some scenarios do not allow you to answer them. Based on the decisions you make, your character will move through the game, dealing with your past decisions. If you type something other than\n'Fight' or 'Flight', the game will not work. If you are not given the option\nto respond, press enter to continue the game. Good luck!")

if explanation_check == "Y":
  print("\nThe first scenario will begin shortly.")
elif explanation_check == "N":
  game_explanation()

scenario_one_print = input("\nYou were camping one day, when a bear was found roaming around your tent.\nUnfortunately, it appears to be agressive, so you don't have much choice\nbut to fight the bear, or run. Type 'Fight' to fight the bear, or 'Flight'\nto run away.\n")

if scenario_one_print == "Fight":
  fight_one = "True"
elif scenario_one_print == "Flight":
  fight_one = "False"

def scenario_one():
  if scenario_one_print == "Fight" :
    print("\nYou chose to fight the bear! It was not much of a competition, for the bear won in an instant. But, you made it out alive, despite it being a very close\ncall.")
  elif scenario_one_print == "Flight" :
    print("\nYou chose to run from the bear! It was a smart decision, because the bear\nimmediately loses interest, and continues to sniff around your tent.\nUnfortunately, your town is known for being full of quarrelsome people, that\nwould probably disagree with your decision. Good thing no one saw you!")

scenario_one()

def scenario_two():
  if fight_one == "True":
    print("\nThe next scenario will begin shortly.")
    print("\nAs you are walking downtown after your recovery, you notice a lumberjack\nwalk by you, and give you a respectful nod. Even though you are slightly\nconfused by this, you can not ignore the fact it feels like you barely\nescaped a dangerous situation. You wonder why he gave you that nod, but\ncontinue on with your day.\n")
  elif fight_one == "False":
    print("\nThe next scenario will begin shortly.")
    print("\nThe world must not be feeling kind to you today. While walking through your neighborhood, a threatening lumberjack approaches you. He explains that he\nwas passing by when he saw you running from the bear. That was a foolish\ndecision. The lumberjack challenges you to a duel! Do you choose to fight or\nrun?")

scenario_two()

if fight_one == "True":
  fight_two = "Pass"
elif fight_one == "False":
  scenario_two_print = input("\nType 'Fight' to accept the duel, or 'Flight' to run away.\n")
  if scenario_two_print == "Fight":
    fight_two = "True"
  elif scenario_two_print == "Flight":
    fight_two = "False"

def scenario_three():
  if fight_two == "True":
    print("\nAlthough you lost the fight, the mayor of your town gives you an award for\ntrying. Turns out, this particular lumberjack is known for picking on random\npeople that are minding their own business. Usually, they run from fear,\n(he was an intimidating guy) so it was a commendable effort.")
  elif fight_two == "False":
    print("\nYou have been shunned from your town for cowardice. They couldn't allow a\nchicken to stay. Would you like to prove the people of your town wrong by\npicking a fight, or leave the town peacefully?")
  elif fight_two == "Pass":
    print("It's been very quiet since your original bear encounter. Maybe luck is on\nyour side today? Either way, it has been a calm few days.")

scenario_three() 

if fight_two == "False":
  scenario_three_print = input("\nType 'Fight' to accept the duel, or 'Flight' to run away.\n")
  if scenario_three_print == "Fight":
    fight_three = "True"
  elif scenario_three_print == "Flight":
    fight_three = "False"
elif fight_two == "True":
  fight_three = "Pass"
elif fight_two == "Pass":
  fight_three = "Pass"
  
def scenario_four():
  if fight_three == "True":
    print("\n\'Twas but a test! You didn't stand a chance against the brutes of your\nvillage, but after discovering you were willing to fight them, they\nwelcome you back with open arms.")
  elif fight_three == "False":
    print("\nYou have been kicked out of your village. It might have been for the best,\nbut now you are in a new town, knowing absolutley no one.")
  elif fight_three == "Pass":
    print("\nIt has been quiet for a while, so you decide to do some snooping. After\nfinding nothing, you ask the universe for something to do. This was a\nmistake. You thought luck was finally on your side? A foolish\nmiscalculation. Within mere seconds, you find yourself surrounded by\nhundreds of minute tasks, all equally important, begging to be completed.\nDo you dare tempt the fates once more by starting a fight with existence\nitself?")
  
scenario_four()

if fight_three == "True":
  fight_four = "Pass"
elif fight_three == "False":
  fight_four = "Pass"
elif fight_three == "Pass":
  scenario_four_print = input("\nDo you chose to fight reality itself? Type 'Fight' to battle the being,\n'Flight' to run away. ")
  if scenario_four_print == "Fight":
    fight_four = "True"
  elif scenario_four_print == "Flight":
    fight_four = "False"

#scenario_four(fight_three, flight_three, pass_three)
#if fight three:
#pass_four
#if flight three:
#pass_three
#if pass_four:
#Fight_four or flight_four
#scenario_five(fight_four, flight_four, pass_four)
#if fight_four:
#flight_five
#if flight_four:
#pass_five
#if pass_four:
#flight or fight five
