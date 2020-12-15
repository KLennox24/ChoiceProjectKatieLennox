
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
  

#scenario_two(fight,flight)
#if flight_one:
#Buff lumberjack laughs at the decision and challenges you
#to a duel
#fight_two, flight_two
#else:
#Passing lumberjack nods in respect after you fought the
#bear
#pass_two (because its part of scenario two)
#scenario_three(flight_two, fight_two, pass_two)
#if flight_two:
#You have been shunned from your village for cowardice.
#Hopefully that doesn’t become important later. Try to
#disagree with village or no
#flight_three fight_three
#if fight_two:
#Although you lost the fight, the mayor of your village
#gives you an award for trying. Usually, they run from
#fear, so it was a commendable effort.
#pass_three
#if pass_two:
#pass_three
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
