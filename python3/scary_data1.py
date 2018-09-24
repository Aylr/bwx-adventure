#!/user/bin/python


from advent import (
    Game,
    Location,
    Connection,
    Object,
    Animal,
    Robot,
    Pet,
    Player,
    Script,
    SayOnSelf,
    Die,
)
from advent import (
    NORTH,
    SOUTH,
    EAST,
    WEST,
    UP,
    DOWN,
    RIGHT,
    LEFT,
    IN,
    OUT,
    FORWARD,
    BACK,
    NORTH_WEST,
    NORTH_EAST,
    SOUTH_WEST,
    SOUTH_EAST,
    NOT_DIRECTION,
)
from advent import Say

game = Game("Scary Data Stories, Volume I")

cubicle = game.new_location(
    "Cubicle", """You are surrounded by beige. A doorway is to the East."""
)

keyboard = cubicle.new_object(
    "keyboard", "a sweet mechanical keyboard with cherry red keys."
)
id_badge = cubicle.new_object(
    "ID badge", "an ID badge with a faded picture of someone named Ben"
)
python_book = cubicle.new_object("python book", "a Python 3 book.")

hallway = game.new_location(
    "Hallway",
    "A long hallway lit with fluorescent lights. A doorway is to the East and West. Noise appears to be coming from a door to the North.",
)
office = game.new_location(
    "Office", "A typical middle manager office with tidy desk and worn executive chair."
)
server_room = game.new_location(
    "Server Room",
    """A cold room filled with racks of loud servers. Blinkenlights surround you.
There is a door to the South.""",
)
game.connect(office, hallway, WEST)
game.connect(cubicle, hallway, EAST)

server_room_door = game.new_connection("Door", hallway, server_room, NORTH, SOUTH)
server_room_door.set_flag("locked")


def use_badge(game, thing):
    game.output(
        "you hold Ben's badge up to the reader and you hear a beep and a click, and see a green light"
    )
    thing.unset_flag("locked")


server_room_door.add_phrase("use badge", use_badge, [id_badge])

# staging = server_room.new_object("staging server", "a loud 1U server.")
server = server_room.new_object("server", "a loud 2U server.", fixed=True)
csv = server_room.new_object("csv", "a dirty csv is lying on the floor.")

server_room.add_phrase(
    "login", Say("You logged into the server. It says Welcome Initech Production.")
)
csv.add_phrase(
    "load csv",
    Die(
        """loading the dirty csv into the server. 8 hours later production goes 
    down. Noone knows why."""
    ),
)


player = game.new_player(hallway)


manager = Animal("manager")
manager.set_location(office)
manager.add_verb(
    SayOnSelf(
        """The manager asks you why the dashboard is still broken and asks
you to go ahead and come in on Saturday to fix it.""",
        "talk",
    )
)
manager.set_allowed_locations([office, hallway, cubicle])


test_script = Script(
    "test",
    """
> go east
> talk manager
> go west
> go west
> take ID badge
> look at ID badge
> look at keyboard
> take keyboard
> go east
> use badge
> go north
> login
> load csv
> end
""",
)
player.add_script(test_script)


game.run()
