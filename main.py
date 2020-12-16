
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

def scenario_five():
  if fight_three == "False":
    print("After a chaotic month, you stop for a bit to look at your life choices. Where has everything you've done led you? A random town? Away from friends of family? A newfound respect for life? Proof of your inner cowardice? What will you do now? What's left? Will you pick up your battered and broken pride and start anew? Or give in to the feeling of fear that has pushed all your choices so far?")
  elif fight_three == "True":
    print("What a month. You've run from a bear, dueled a strange man, and earned the respect of everyone around you. What comes next? Running for mayor? Facing that dreaded bear once more? A life full of pride and victory? Learning from mistakes? No one can decide this but you, so pick a good life to lead.")
  elif fight_four == "True":
    print("It was quiet life you led, but it certainly ended with lots of excitement. How you thought you could beat reality itself will be a mystery for ages to come, but there is some worth in what you have done so far. Albeit it wasn't much. You pretty much dodged every interesting bit of life that was thrown at you. Would you like to try again?")
  elif fight_four == "False":
    print("A reasonable answer, it would have been interesting if you tried. You continue on with your life, completing all those tasks that appear to have piled up. They take you through a life full of happiness and success. When your days come to an end, you ponder over the strangest decisions you've made in your lifetime. The brawl with the bear comes back to you. As your existence begins to fade as a sign of your age, you begin to wonder. What would have happened if you made a different choice?")

scenario_five()

if fight_three == "False":
  scenario_five_print_one = input("\nType 'Start Anew' to start a life in your new town, or 'Give In' to try to go home one last time.")
elif fight_three == "True":
  scenario_five_print_two = input("\nType 'Mayor' to try to run for mayor, or type 'Final Boss Fight' to go looking for the bear you ran from in the beginning.")
elif fight_four == "True":
  scenario_five_print_three = input("\nType 'Try Again' to try different routes of the life you led, or type 'Accept Failure' to accept you have failed in this timeline and will eternally stare into the abyss as the result of your actions.")
elif fight_four == "False":
  scenario_five_print_four = input("\nType 'Alternate Route' to try your life again from your original encounter, or 'Accept Success' to leave things as they are.")