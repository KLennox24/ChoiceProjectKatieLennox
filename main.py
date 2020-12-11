
scenario_one_print = input("You were camping one day, when a bear was found roaming around\nyour tent. Unfortunately, it appears to be agressive, so you\ndon't have much choice but to fight the bear, or run. Type\n'Fight' to fight the bear, or 'Flight' to run away.\n")

if scenario_one_print == "Fight":
  fight_one = "True"
elif scenario_one_print == "Flight":
  fight_one = "False"

def scenario_one():
  if scenario_one_print == "Fight" :
    print("You chose to fight the bear! It was not much of a competition, for the bear won in an instant. But, you made it out alive, despite it being a very close\ncall.")
  elif scenario_one_print == "Flight" :
    print("You chose to run from the bear! It was a smart decision, because the bear\nimmediately loses interest, and continues to sniff around your tent.\nUnfortunately, your town is known for being full of quarrelsome people, that\nwould probably disagree with your decision. Good thing no one saw you!")

scenario_one()

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
