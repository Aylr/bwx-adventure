#Castle adventure game tutorial

# First we import all of the functions from the advent.py module.  This module holds all
# of the functions we need to create our adventure game!

from advent import *

# The star (*) in the line above just means that we want to import everything from the
# advent.py module

# We now create a new game.  Let's call it "Castle Adventure".

game = Game("Castle Adventure")

# The lower case "game" is the variable that will contain all of the rooms and connections.
# The upper case "Game" is a function that assigns "game" all of the functions we will
# need to create our game.

# Before we start creating rooms, lets set the scene for the player by writing a short
# 'splash screen'.  The splash screen is what pops up before the game starts to let you
# know what's going on and what you're supposed to be doing.

# We are going to use the set_splash function of the "game" variable.  This is just one
# of the many functions that "game" now has thanks to the "game = Game("Castle Adventure")"
# command we used above.

game.set_splash("""You stand outside a disheveled and un-kept castle.
The water in the moat is dirty and turgid, and there are weeds growing
everywhere.  This once beautiful castle has fallen into ruin.

Legend has it that 100 years ago a mighty king lived in this castle.
This king fought and conquered many of the surrounding kingdoms and
brought all of his treasures back to this castle.

One day, the mighty king heard of a dragon living in the mountains near by.
It was said that the dragon lay on a mighty hoard of treasure.  Unable to
contain himself, the king rushed off and challenged the dragon to a duel.

Unfortunately for the king, the dragon ate him.  The dragon then flew to the
castle and ate everyone who was there.  The dragon then collected up all
of the kings treasure and sat on it.

Your job is to kill the dragon and find the kings crown.  Then you can rule
this land!""")

# That's a lot of words.  You might want to make your on splash screen a bit shorter.
# The three quotation marks in a row ' """ ' allow you to write text that goes over more
# than one line.  If we had used a single quote ' " ' then we would have to have kept
# all the text on one line (which makes it hard to read).  If we had have used one quote
# and written text on more than one line, Python would get confused and throw up an error.

# OK.  That was fun.  Now lets make a bunch of locations (otherwise known as rooms) for
# our adventure.  To do this we are going to create variables that we are going to assign
# the Location object.  This object takes three variables: the name of the location, a
# description of the location, and a final variable that tells the program how to
# describe the location.  For example, are you "in" the bedroom, or "on" the drawbridge?



#  ----  Location descriptions ----

drawbridge = Location("Drawbridge", """You are standing on the drawbridge outside the castle.
The dirty water from the moat swirls beneath your feet.
The main gates to the castle hang open.
You will have to go in as there is no way back now""", "on")

courtyard = Location("Courtyard", """You are in a dirty and muddy courtyard.  No-one has been
in here for years.  There are weeds everywhere.
In the centre of the courtyard is a well.
Beyond the well are the great doors to the keep.
To the west is a dilapidated building with 'Store' written on it.
To the east is a shed that looks like a black smith's workshop.""", "in")

# You can create locations whose description depends on certain events in the game.  In
# this case, we want the well to be full of water until a lever in the dungeon is pulled.
# We do this by adding a new variable, "well_description" which changes its output depending on the value
# of a game switch.  The default for the game switch is false.

def well_description(self):
    return ["""You are in the centre of the courtyard.
In front of you is a well. """, game.if_flag("well_full", "The well is empty!  You see a ladder leading down.\n",
                                             "The well is full of dirty water.\n",
                                             dungeon),
                         """To the north are the main doors to the keep.
To the west are some smelly stables.
To the east is a stone building with 'Food store' written on it."""]

well = Location("Well", well_description, "at")

# The "def" tells Python that we're defining a new variable, in this case called "well_description".
# The if_flag function of the "game" variable as four inputs:
# 1. The name of the flag, in this case "well_full"
# 2. What to say if the flag is true
# 3. What to say if the falg is false
# 4. Which location the flag is associated with (in this case a lever in the dungeon).

dungeon = Location("Dungeon", ["""You are in a dark and creepy dungeon.
Small animals skitter around your feet.\n""",
  game.if_flag("well_full", "There is a rusty old lever here in the up position.\n",
               "There is a rusty old lever here in the down position.\n"),
"The only way out is back up the stairs."], "in")

dungeon_stairs = Location("Stairs", """There are stairs leading down into darkness.
I don't think you should go down there without a light of some kind...""", "on")

lab = Location("Secret lab", """The ladder leads down to a tunnel under the courtyard!
The tunnel leads to a secret lab filled with mysterious devices.
Don't touch anything!  You never know what might happen!.""", "in")

store = Location("Store", """You are in a broken-down old store house.
There's nothing much of use left here - I guess most of it has been stolen.
There is some wood stacked in the corner.
The only exit is back out through the door you came in.""", "in")

smithy = Location("Smithy", ["""You are in the old smithy.
There's nothing much left here - all the armour and weopons are gone.\n""",
                             game.if_flag("furnace_lit", "The old furnace has a small fire going in it.\n",
                                          "There is an old furnace here that has long since gone out.\n"),
                             """The only exit is back out through the door you came in."""], "in")

stables = Location("Stables", """This has to be the smelliest part of the castle.
I mean, really - you would think that the stink would have died down by now.
Pwew - that is bad.  I think the smell might be coming from that pile of rotten hay in the corner.
The only way out is back through the door you came in.""", "in")

food_store = Location("Food store", """This cold stone building used to store all of the castle's food.
Now there's not much left - a few mouldy sacks of grain and an
old roast that's so smelly that even the rats haven't eaten it.""", "in")

keep_entrance = Location("Keep entrance", """You are at the north end of the courtyard
in front of the great doors to the keep.
To be honest, they don't look so great from close up.
The well is behind you to the south.""", "at")

hall_south = Location("South end of hall", """You are at the south end of a grand hall.
There are doorways to the east and west.
To the north is a great table that appears to have been set for a feast.
In the distance you can hear a deep rumbling...""", "in")

bedroom = Location("Bedroom", """This looks like a once-grand bedroom.
Now, though, it's just dusty and mouldy.  Not nice.
There's an old four-poster bed in the middle of the room.
You're about to look away when you think you see something under the bed!
The exit is to the east.""", "in")

under_bed = Location("Under the bed", """You are hiding uder the great four-poster bed.
This isn't very hero-like is it?
It's a bit dark, but one of the floor boards looks a bit funny...""", "in")

hall_middle = Location("Middle of the hall", """You are in the middle of the grand hall.
There is a great table here that looks like it was once set for a feast.
Now, though, there is nothing left of that feast but a few mouldy scraps.
There are doors to the east and west.
To the north the rumbling nouse is louder!
There might be a great dragon asleep on a pile of treasure to the north but you can't be sure...""", "at")

def library_description(self):
    if "large book" in game.player.inventory:
        return """You are in a musty old library.
There are books everywhere - in shelves and scattered all over the floor.
The exit is to the east."""
    else:
        return """You are in a musty old library.
There are books everywhere - in shelves and scattered all over the floor.
One book captures your eye - it's title is 'How to Kill a Dragon'!
The exit is to the east."""

library = Location("Library", library_description, "in")

kitchen = Location("Kitchen", """This is the kitchen where the great feasts were prepared.
Now, there's nothing here but rats and old scraps of meat.
The exit is to the west.""", "in")

hall_north = Location("North end of the hall", ["You are at the northen end of the great hall.\n",
                                                game.if_flag("dead_dragon", """The dragon lies dead at your feet!
There is a pile of treasure here, and behind the thone you can see another exit!\n""",
                                                             """There is an enormous dragon here, lying on a large pile of treasure.
The rumbling sound is the sound of the dragon snoring!
There might be an exit behind the dragon but you can't tell because the dragon is blocking the exit!\n"""),
                                                "The great table is behind you to the south."]
                                                             , "at")

behind_throne = Location("Behind the throne", "There is a door here leading up to the tower.", "at")

tower = Location("Tower", """Narrow windy stairs lead up to a tall tower behind the keep.
You have a great view of the surrounding country side from this tower!
On a pillow in the centre of the tower you see the kings crown!
You pick up the crown and put it on your head - you are now the king!""", "at")

# Once we have created all of our locations, we have to add them to the game.  We use the
# add_location function of the "game" variable.


#  ----  Add locations to the game  ----

game.add_location(drawbridge)
game.add_location(courtyard)
game.add_location(well)
game.add_location(dungeon)
game.add_location(dungeon_stairs)
game.add_location(lab)
game.add_location(store)
game.add_location(smithy)
game.add_location(stables)
game.add_location(keep_entrance)
game.add_location(hall_south)
game.add_location(bedroom)
game.add_location(hall_middle)
game.add_location(library)
game.add_location(kitchen)
game.add_location(hall_north)
game.add_location(tower)
game.add_location(under_bed)
game.add_location(food_store)
game.add_location(behind_throne)

#  ----  Add the win location  ----
tower.set_win(True)


# Add game connections.  Now we connect our rooms to each other, so that we can travel between them.  We use the
# simple "connect" function of the "game" variable to do this for us.  The "connect" function takes three
# arguments: the first two are the locations to be joined, and the third is the direction that joins the first
# location to the second.


#  ----  Add connections between rooms  ----

game.connect(drawbridge, courtyard, [IN, NORTH])
game.connect(courtyard, well, NORTH)
game.connect(courtyard, store, WEST)
game.connect(courtyard, smithy, EAST)
game.connect(well, stables, WEST)
game.connect(well, food_store, EAST)
game.connect(well, keep_entrance, NORTH)
game.connect(keep_entrance, hall_south, NORTH)
game.connect(hall_south, bedroom, WEST)
game.connect(hall_south, dungeon_stairs, EAST)
game.connect(dungeon_stairs, dungeon, DOWN)
game.connect(hall_south, hall_middle, NORTH)
game.connect(hall_middle, library, WEST)
game.connect(hall_middle, kitchen, EAST)
game.connect(hall_middle, hall_north, NORTH)
game.connect(behind_throne, tower, [NORTH, UP])
#game.connect(well, lab, DOWN)
#game.connect(bedroom, under_bed, DOWN)

del dungeon_stairs.exits[DOWN]


# That's nice, but not very interesting.  You've created rooms and connections but all you can do is wonder
# around and look at things.  Now lets add some objects to the game to make it interesting...  First of all we
# creat our objects using the "Object" function, and then we add them to specific locations.  An Object can have
# three arguments: a short description of the object, a long description of the object, and a flag which indicates
# whether you can take the object or not.

#  ---- Create our objects  ----

wood = Object("wood", "rotten wood - it doesn't look like it will burn well...")
hay = Object("hay", "mouldy hay - this might burn but you will need to combine it with something...")
dungeon_key = Object("dungeon key", "a black and rusty key")
flint = Object("flint", "a small piece of flint")
tower_key = Object("tower key", "a beautiful golden key")
knife = Object("carving knife", "a blunt and rusty carving knife - I wouldn't try attacking anything with this")
book = Object("large book", "a dusty old book with the bold title claiming to explain how to kill dragons!")
unlit_torch = Object("torch", "a somewhat shoddily crafted, but servicable, torch")
lit_torch = Object("torch", "a flickering and spluttering torch providing little light")
meat = Object("meat", "a large hunk of rotting meat", True)

# Food and drink are special objects that can be consumed.  They create new objects after they have been eaten or
# drunk.  You can also add an action that happens after the player consumes one of these items (like dying).
# Let's create a food item and a drink item

steak = Food("steak", "rotten steak - I wouldn't eat this if I were you",
             Die("""chewing on the rotten steak and start to feel queasy.
I really don't think you should have done that.
You stagger about for a while feeling sick until you keel over and die."""))

poison = Drink("poison", "thick and gooey blue-green poison in a bottle",
                Die("chugging down the posion.  It's poison!  Aaarrgh!  You die!"))


dragon_bait = Food("dragon bait", """the steak has turned an odd shade of purplse.
I really wouldn't eat it now.""",
                     Die("chewing the poisened steak.  Really?  You die."))

#  ----  Add objects to locations  ----

store.add_object(wood)
stables.add_object(hay)
kitchen.add_object(knife)
food_store.add_object(meat)
lab.add_object(poison)
library.add_object(book)
hall_middle.add_object(flint)

# Not all objects have to be in locations.  Some can be in 'containers'.  Containers are special objects that
# can't be taken, but can be opened by the player to find other objects.  Containers can be locked or unlocked.
# We're going to add a container under the bed that has the key to the dungeon in it.  Containers have to be
# added to specific locations (in this case, under the bed).


#  ----  Create containers  ----

floor_board = under_bed.add_object(Container("loose floorboard", """this floorboard looks loose.
With some jiggling you might be able to open it!"""))

floor_board.add_object(dungeon_key)

# Certain locations can be locked until you have the right object in your inventory.  In this case, we're going
# to lock the door to the dungeon.  You need to find the dungeon key (in the loose floorboard under the bed)
# before you can enter the dungeion...


#  ----  Create entry conditions  ----

dungeon_stairs.make_requirement(dungeon_key)
tower.make_requirement(tower_key)


# Now you can create special commands for entering certain locations: for example climbing under the bed.
# You can make these special commands dependent on a condition - for example, you can only climb down the
# well if the water has been drained first...


#  ----  Special entry methods  ----

def climb_under_bed(game, thing):
    game.output("You climb under the bed")
    game.player.set_location(under_bed)

bedroom.add_phrase("climb under bed", climb_under_bed)
bedroom.add_phrase("go under bed", climb_under_bed)

def climb_out_bed(game, thing):
    game.output("You climb out from under the bed")
    game.player.set_location(bedroom)

under_bed.add_phrase("climb out", climb_out_bed)
under_bed.add_phrase("get out", climb_out_bed)

def climb_down_well(game, thing):
    if 'well_full' in dungeon.vars:
        game.output("You climb down the ladder into darkness...")
        game.player.set_location(lab)
    else:
        game.output("You can't climb down the well - it's full of dirty water!")

well.add_phrase("climb down well", climb_down_well)
well.add_phrase("climb down", climb_down_well)

def climb_out(game, thing):
    game.output("You climb out of the well")
    game.player.set_location(well)

lab.add_phrase("climb out", climb_out)
lab.add_phrase("climb ladder", climb_out)
lab.add_phrase("climb well", climb_out)
lab.add_phrase("climb up", climb_out)

def climb_down_stairs(game, thing):
    if 'torch_lit' in smithy.vars:
        game.output("You climb gingerly down the stairs...")
        game.player.set_location(dungeon)
    else:
        game.output("You can't climb down the stairs, it's too dark!")

dungeon_stairs.add_phrase("d", climb_down_stairs)
dungeon_stairs.add_phrase("down", climb_down_stairs)
dungeon_stairs.add_phrase("climb down", climb_down_stairs)
dungeon_stairs.add_phrase("climb stairs", climb_down_stairs)

def get_past_dragon(game, thing):
    if dragon.health == -1:
        game.player.set_location(behind_throne)
    else:
        game.output("""The dragon wakes up as you try to sneak past him!
This makes the dragon quite angry, so he eats you.""")
        game.player.terminate()

hall_north.add_phrase("n", get_past_dragon)
hall_north.add_phrase("north", get_past_dragon)
hall_north.add_phrase("North", get_past_dragon)

# Add special actions at locations
# When a flag is set, it creates a var in the Base Object.  When the flag is un-set it deletes the var - so you
# can't check that it's there because it's been deleted - you will get an error.  To check if the flag has
# been set just check to see if it exists in the list of vars.

def cut_meat(self, actor, noun, words):
    if (noun and noun != "meat"):
        return False
    if "carving knife" in game.player.inventory:
        print("""You cut a steak off the meat.
The rest of the meat falls apart and is useless to you now.""")
        del actor.location.contents['meat']
        actor.location.add_object(steak)
        return True
    else:
        print("You've got nothing to cut the meat with.")
        return False

food_store.add_verb(Verb(cut_meat, "cut"))
food_store.add_verb(Verb(cut_meat, "carve"))

def pull(self, actor, noun, words):
  if (noun and noun != "lever") or words:
    return False
  if self.flag('well_full'):
    self.unset_flag('well_full')
    print("You pull the lever down and hear a gurgling sound coming from somewhere outside.")
  else:
    self.set_flag('well_full')
    print("You pull the lever up and hear a rushing sound coming from somewhere outside.")
  return True

dungeon.add_verb(Verb(pull, 'pull'))

def read(self, actor, noun, words):
    if (noun and noun != "large book") or words:
        return False
    if not self.flag('book_read'):
        self.set_flag('book_read')
        print("""You flip through the book but it doesn't say anything about how to fight a dragon!
The author seems to think that the only way to kill a dragon is to make dragon bait
by poisoning some meat with a special dragon poison...
As you are flipping through the book, something falls out and lands on the ground!""")
        actor.location.add_object(tower_key)
    else:
        print("""You flip through the book but it doesn't say anything about how to fight a dragon!
The author seems to think that the only way to kill a dragon is to make dragon bait
by poisoning some meat with a special dragon poison...""")
    return True

book.add_verb(Verb(read, "read"))

def start_furnace(self, actor, noun, words):
    if (noun and noun != "furnace") or words:
        return False
    if "flint" in game.player.inventory:
        self.set_flag('furnace_lit')
        print("You use the flint to light the furnace!")
    else:
        print("You will need something to help you light the furnace...")
    return True

smithy.add_verb(Verb(start_furnace, "start"))

def look_at_furnace(self, actor, noun, words):
    if (noun and noun != "furnace"):
        return False
    if self.flag('furnace_lit'):
        print("A small fire is bravely flickering in the furnace.")
    else:
        print("You could probably start this furnace, but you would need something to get it going.")
    return True

smithy.add_verb(Verb(look_at_furnace,"look at"))

def light_torch(self, actor, noun, words):
    if not 'furnace_lit' in self.vars:
        print("The furnace hasn't been lit.")
        return False
    if (noun and noun != "torch") or words:
        print("I don't think that's a good idea")
        return False
    if not "torch" in game.player.inventory:
        print("You don't have the torch!")
        return False
    if not self.flag('torch_lit'):
        print("You light the torch in the furnace!")
        game.player.remove_from_inventory(unlit_torch)
        game.player.add_to_inventory(lit_torch)
        self.set_flag('torch_lit')
        self.set_var('torch_time',10)
        return True
    else:
        print("the torch is already alight.")
        return False

smithy.add_verb(Verb(light_torch, "light"))

def look_under_bed(self, actor, noun, words):
    if (noun and noun != "bed"):
        return False
    print("""It's a bit dark - you can't quite see.
You might have to climb under the bed to have a closer look.""")
    return True

bedroom.add_verb(Verb(look_under_bed, "look under"))

# Recipes

torch_recipe = Recipe("torch", unlit_torch, [wood, hay], "You wrap the hay around the wood to make a torch!")
game.add_recipe(torch_recipe)

dragon_bait_recipe = Recipe("dragon bait", dragon_bait, [steak, poison], """You pour the poison onto the meet.
The meat bubbles and turns a strange shade of purple.""")
game.add_recipe(dragon_bait_recipe)

# Add the dragon

dragon = Actor("large, nasty dragon")
dragon.set_location(hall_north)
game.add_actor(dragon)

def fight_dragon(self, actor, noun, words):
    if (noun and noun != "dragon"):
        print("You can't fight a %s." % noun)
        return False
    if not "carving knife" in game.player.inventory:
        print("What with?  Your bare hands?  Don't be silly")
        return False
    else:
        print("""You bravely attack the dragon with the carving knife.
Unfortunately, all that happens is that the dragon wakes up and gets angry.
The dragon eats you.""")
        game.player.terminate()
    return True

hall_north.add_verb(Verb(fight_dragon, "fight"))

def throw_meat(self, actor, noun, words):
    if not noun:
        return False
    if noun == "steak":
        if not "steak"  in game.player.inventory:
            print("You don't have the steak")
            return False
        else:
            print("""You throw the steak at the dragon.
Unfortunately, the dragon seems to have a stronger constitution than you.
The dragon eats the steak.  Now that the dragon is awake,
he eyes you off... and then eats you.""")
            game.player.terminate()
            return False
    elif noun == "dragon bait":
        if not "dragon bait" in game.player.inventory:
            print("You don't have the dragon bait.")
            return False
        else:
            print("""You throw the dragon bait in the air.
The dragon raises his head and grabs it out of the air and swallows it!
The dragon looks at you strangley and then crosses his eyes.
The dragon burps and purple smoke curls out of his mouth.
Then he dies.""")
            dragon.terminate()
            return True
    else:
        print("I wouldn't throw that.")
        return False

hall_north.add_verb(Verb(throw_meat, "throw"))

hero = game.new_player(drawbridge)

# Add special phrases

steak.add_verb(SayOnSelf("Try: make dragon bait", "poison"))

# Add update function

def update():
    if 'torch_lit' in smithy.vars:
        if not 'torch' in game.player.inventory:
            print("The torch splutters, goes out, and then falls apart.")
            smithy.unset_var('torch_time')
            smithy.unset_flag('torch_lit')
            del game.player.location.contents['torch']
            store.add_object(wood)
            stables.add_object(hay)
    if 'torch_time' in smithy.vars:
        if smithy.var('torch_time') == 0:
            print("The torch splutters, goes out, and then falls apart.")
            if game.player.location == dungeon:
                print("""You are plunged into darkness...
Suddenly you hear a horrible scraping noise as
some terrible beast slithers out of the darkness.
It gobbles you up.""")
                game.player.terminate()
            else:
                smithy.unset_var('torch_time')
                smithy.unset_flag('torch_lit')
                game.player.remove_from_inventory(lit_torch)
                store.add_object(wood)
                stables.add_object(hay)
        else:
            smithy.set_var('torch_time', smithy.var('torch_time')-1)


game.run(update)
