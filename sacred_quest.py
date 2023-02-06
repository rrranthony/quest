import random

character_stats = {
    "perception": 0,
    "luck": 0
}

key_item = {
    "sword": "no",
    "orb": "no",
    "cloak": "no",
    "hilt": "no"
}

secondary_item = {
    "bloodstone": "no",
    "ring_of_power": "no"
}

hermits = {
    "hermit_hogbog1": "alive"
}

orb = {
    "power": 0
}

cloak = {
    "golden": "no"
}

mountains = {
    "porcupine_pass": "no"
}


def get_user_choice(choices):
    """Return the choice from the user, selected from the given choices.

    choices must be a list of strings.
    """
    choices_prompt = ", ".join(choices)

    while True:
        print("(Type: " + choices_prompt + "): ", end="")
        user_choice = input()
        if user_choice in choices:
            return user_choice


def mountains_porcupinepass():
    print('Navigating a ridge, the ground suddenly feels softer and fleshy')
    print('Suddenly stone needles jut from the earth until you are surrounded.')
    print('How do you try to escape?')
    options = ['fight through', 'tickle']
    userInput = get_user_choice(options)
    if userInput == 'fight through':
        if key_item['sword'] == 'yes':
            print('As you slash the first spike you hear a monstrous roar and the earth shakes...')
            print('You are atop a Colossal Porcupino!  Bloodied, you roll downhill...')
            #river_crossroads
        elif key_item['orb'] == 'yes' and orb['power'] > 0:
            print('A blast of magical power cleanly severs the spikes in your path and you voyage onward')
            mountains['porcupine_pass'] = 'passed'
            mountain_crossroads()
        elif key_item['orb'] == 'yes':
            print('Your orb fizzles as if missing some vital ingredient.  You are stranded until...')
            print('This section of the mountain breaks loose and begins walking downhill')
            print('You are atop a Colossal Porcupino!')
            #river_crossroads
        elif key_item['cloak'] == 'yes':
            print('Your cloak catches on the spikes and you are unable to pull yourself free.')
            print('This section of the mountain breaks loose and begins walking downhill')
            print('You are atop a Colossal Porcupino!')
            #river_crossroads
        elif cloak['golden'] == 'yes':
            print('As you step forward, the gold cloak suddenly lifts you upward and over the spikes.')
            print('It gently sets you down on the other side.')
            mountains['porcupine_pass'] = 'passed'
            mountain_crossroads()
    elif userInput == 'tickle':
            print('Not pausing to ask why, you start tickling the needles and the fleshy earth under them.')
            print('You hear a rumbly squeaking underground, and all the spikes retract, leaving the path clear.')
            mountains['porcupine_pass'] = 'passed'
            mountain_crossroads()
    else:
        print('You hesitate...')
        mountains_porcupinepass()

def mountain_crossroads():
    mountain_paths = random.randint(1,5)
    if mountain_paths == 1:
        if mountains['porcupine_pass'] == 'passed':
            mountain_crossroads()
        else:
            mountains_porcupinepass()
    elif mountain_paths == 2:
        mountains_rockslide()
    elif mountain_paths == 3:
        mountains_destinycliff()
    elif mountain_paths == 4:
        mountains_shrine()
    elif mountain_paths == 5:
        mountains_well()

def lunch_hermitcave():
    print('The codworms pop between your teeth as you sit on a mossy stone in the cave')
    print('-What are you seeking, traveler?- Hogbog asks.\n')
    answers = ['seek power', 'seek love', 'seek mystery']
    userInput = get_user_choice(answers)
    if userInput == 'power':
        print('-I sought power once- Hogbog whispers into the cooking fire.')
        print('He pulls out a gold ring from his ragged tunic and fondles it with a look of madness.')
        print('Suddenly he throws it at you!')
        print('-Take it!- he cries, and you find it has latched onto your finger, and the hermit is gone.')
        secondary_item['ring_of_power'] = 'yes'
        mountain_crossroads()
    elif userInput == 'love':
        print('-Love guides us all...if we allow it- Hogbog whispers into the cooking fire.')
        if key_item['sword'] == 'yes':
            print('-Allow me to help you- Hogbog says, taking your sword and holding it into the flame.')
            print('The sword burns until only the hilt remains and he hands it back to you.')
            key_item['sword'] = 'no'
            key_item['hilt'] = 'yes'
            mountain_crossroads()
        elif key_item['orb'] == 'yes':
            print('-Allow me to help you- Hogbog says, taking your orb and holding it above the flame.')
            print('The orb glows with an inner light and he hands it back to you.')
            orb['power'] = 1
            mountain_crossroads()
        elif key_item['cloak'] == 'yes':
            print('-Allow me to help you- Hogbog says, taking your cloak and flapping it above the flame.')
            print('The cloak changes from black to gold and he hands it back to you.')
            cloak['golden'] = 'yes'
            mountain_crossroads()
    if userInput == 'mystery':
        print('-Mystery...- Hogbog whispers into the cooking fire.')
        print('The flame suddenly blazes a crimson blue and a blinding wind blows through the cave.')
        print('When you open your eyes, the cave and the hermit are gone.')
        character_stats['luck'] += 1
        if character_stats['luck'] >= 0:
            print('You feel a strange sensation...')
        mountain_crossroads()
    else:
        print('-Go on, speak the truth- Hogbog says.')
        lunch_hermitcave()

def loot_hermitcave_hogbog1():
    print('You enter the shallow cave where a pot of codworms sizzle over a fire.')
    if character_stats['perception'] >= 3 or random.randint(1,3) == 1:
        print('You discover a secret alcove with a Bloodstone inside before leaving.')
        print('[Item Aquired: Bloodstone]')
        secondary_item['bloodstone'] = 'yes'
        mountain_crossroads()
    else:
        print('You scald your tongue on the stew and kick it over before leaving.')
        mountain_crossroads()


def mountain_miser_encounter():
    print('As you venture uphill and the trees thin, you see a haggard hermit peeking at you from a cave.\n')
    print('Your heart quickens.  What will you do?')
    actions = ['attack','befriend']
    userInput = get_user_choice(actions)
    if userInput == 'attack':
        if key_item['sword'] == 'yes':
            print("With a single slash you cut the lonely soul down.\n")
            print("-What have I done?- the hermit gasps as his eyes close forever.")
            hermits['hermit_hogbog1'] = "dead"
            loot_hermitcave_hogbog1()
        elif key_item['orb'] == 'yes':
            print("The orb crackles in your hand and fizzles out.\n")
            print("In horror the hermit flees for his life downhill and disappears.")
            loot_hermitcave_hogbog1()
        elif key_item['cloak'] == 'yes':
            print("Your cloak billows as you approach and the hermit is paralyzed in fear.\n")
            print("He falls dead before you from heart attack")
            hermits['hermit_hogbog1'] = "dead"
            loot_hermitcave_hogbog1()
    elif userInput == 'befriend':
        print('\n-Walahazoo young traveler! I am Hogbog the Hermit and this is my cave-')
        print('-I dont have much, but I have a lunch of codworms.  Come share it with me.\n')
        lunch_hermitcave()
    else:
        print('You hesitate...')
        mountain_miser_encounter()


def first_item_Scene():
    print('You can only carry one item.  Choose wisely:\n')
    items = ['sword','orb','cloak']
    userInput = get_user_choice(items)
    if userInput == 'sword':
        print('\nWooden sword of the sprites!')
        print('You are destined to be a warrior!  Dont be clumsy with that...\n')
        key_item['sword'] = 'yes'
        firstpath_choice()
    elif userInput == 'orb':
        print('\nOrb of the mage frogs!')
        print('Clutch it with the webby hand of a wizard!  Beware its power...\n')
        key_item['orb'] = 'yes'
        firstpath_choice()
    elif userInput == 'cloak':
        print('\nCloak of darkness!')
        print('Mysterious one you are!  Can you be trusted?...\n')
        key_item['cloak'] = 'yes'
        firstpath_choice()
    else:
        print('I must have water in my ears.  What was that again?\n')
        first_item_Scene()

def firstpath_choice():
    print('Very good.  But the path splits here.  Will you go toward the mountains or the river?\n')
    firstpath_choices = ['mountains','river']
    userInput = get_user_choice(firstpath_choices)
    if userInput == 'mountains':
        print('\nTaking the high-ground! It will strengthen you, if you do not fall!')
        mountain_miser_encounter()


#ADVENTURE BEGINS

print("Whatup homeboy. I'm Zig. What do you call yourself?\n")

name = input("(Enter your name): ")

if name.lower() == 'zag':
    print('Zagulous!  My long lost brother!  I thought you were dead!')
else: 
    print((name) + '! What kind of name is that?!')

print('Well, anyway. To business. We find ourselves in the sacred forest\n')


first_item_Scene()



