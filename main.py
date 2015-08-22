# Code the classes and a test to run them
from sys import exit
from random import randint

def quit():
    print ''
    print bcolors.GREEN + 'BYE!' + bcolors.END
    print ''
    exit(1)

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):
    quips = [
        bcolors.RED + "\nYou died. You kinda suck at his.\n" + bcolors.END,
        bcolors.RED + "\nYour mom would be proud... if she were smarter.\n" + bcolors.END,
        bcolors.RED + "\nSuch a looser...\n" + bcolors.END,
        bcolors.RED + "\nI have a small puppy that's better at this.\n" + bcolors.END
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print bcolors.GREEN + "\n The Gothons of Planet Percal #26" + bcolors.END
        print bcolors.BLUE + "\nThe Gothons of Planet Percal #26 have invaded your ship and destroy"
        print "your entire crew. You are the last surviving member and your last"
        print "misson is to get the neutron destruct bomb from the Weapons Armory"
        print "put it in the bridge, and blow the ship up after getting into"
        print "escape pod."
        print ""
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clow"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you." + bcolors.END
        print ''
        action = raw_input("> ")

        if  "shoot" in action:
            print bcolors.YELLOW + "\nQuick in the draw you yank out your blaster abd fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim. Your laser hits his costume but misses him entirely. This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast youre repeatedly in the face until"
            print "you are dead. Then he eats you." + bcolors.END
            return 'death'

        elif "dodge" in action:
            print bcolors.YELLOW + "\nLike a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head abd eats you." + bcolors.END
            return 'death'

        elif action == "tell a joke":
            print bcolors.YELLOW + "\nLucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothin stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door." + bcolors.END
            return 'laser_weapon_armory'

        elif action == "exit" or guess == "quit":
            quit()

        else:
            print bcolors.YELLOW + "\nDOES NOT COMPUTE!" + bcolors.END
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print bcolors.BLUE + "\nYou do a drive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "nutron bomb in its container. There's a keypad lock on the box"
        print "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb. The code is 3 digits." + bcolors.END
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("\n[keypad]> ")
        guesses = 0
        cheat = str(666)

        while (guess != cheat and guess != code) and guesses < 9:
            print "BZZZZEDD!"
            guesses += 1
            guess = raw_input("\n[keypad]> ")

        if guess == cheat or guess == code:
            print bcolors.YELLOW + "\nThe container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bidge where you must place it in the right spot." + bcolors.END
            return 'the_bridge'

        elif guess == 'exit' or guess == 'quit':
            quit()

        else:
            print bcolors.YELLOW + "\nThe lock buzzes on last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit therem and finally the Gothons blow up the"
            print "ship form their ship and you die." + bcolors.END
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print bcolors.BLUE + "\nYou burst onto the Bridge with the neutron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off." + bcolors.END

        action = raw_input("\n> ")

        if action == "throw the bomb":
            print bcolors.YELLOW + "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door. Right as you drop it a"
            print "Gothon shoots you right in tha back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off." + bcolors.END
            return 'death'

        elif action == "slowly place the bomb":
            print bcolors.YELLOW + "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can." + bcolors.END
            return 'escape_pod'

        else:
            print bcolors.YELLOW + "\nDOES NOT COMPUTE!" + bcolors.END
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print bcolors.BLUE + "\nYou rush through the ship desperately trying to make is to"
        print "the escape pod before the whole shipe explodes. It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you don't have time to look. There's 5 pods, which one"
        print "do you take?" + bcolors.END

        good_pod = randint(1,5)
        guess = raw_input("\n[pod #]> ")

        if int(guess) != good_pod:
            print bcolors.YELLOW + "\nYou jump into pod %s and hit the eject button." % guess + bcolors.END
            print bcolors.YELLOW + "The pod escapes out into the void of space, then"
            print "impodes as the hull rupters, crushing your body"
            print "into jam jelly." + bcolors.END
            return 'death'
        else:
            print bcolors.YELLOW + "\nYou jump into pod %s and hit the eject button." % guess + bcolors.END
            print bcolors.YELLOW + "The pod easily slides out into space heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time. You won!" + bcolors.END

            return 'finished'

class Finished(Scene):

    def enter(self):
        print bcolors.GREEN + "\nYou won! Great job!" + bcolors.END
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
