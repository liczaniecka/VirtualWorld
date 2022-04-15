# VirtualWorld


This is my very first project in Python, back in May 2021, hence there are some notation mistakes and hard-to-read code. 

The main goal of the project was the implementation of a 2D virtual world simulator. The virtual
world has the structure of a two-dimensional NxM grid. In this world, simple life
forms exist, each with different behaviour depending on its species. Every organism
occupies exactly one cell of the world's 2D grid array. Each cell contains no more
than a single organism at one time (in case of a collision, one of the organisms is
removed from the cell).

All actions in the simulator are performed in turns. During each turn, every living
organism in the world performs an action appropriate to its kind. Some of them
move (animals), while others remain static (plants). In case of a collision (one of the
organisms enters a cell occupied by another organism), one of them wins, either by killing its
opponent (i.e. wolf) or by reflecting the opponent's attack (i.e. turtle). The order of all actions
during a single turn depends on the initiative of each living organism. Animals with the
highest initiative move first. In the case of animals with the same initiative, the order is
determined by the animal's age (the oldest animal moves first). In case of a collision, the
victory depends on the strength of both organisms -> stronger organism wins (with some
exceptions, eg. turtle). In the case of equal strength, the encounter is won by the attacker. The
game also includes a human player, who is a specific kind of animal. Unlike regular
animals, his movement is not random. Instead, the direction of the human's movement is
determined by the player by pressing the appropriate arrow key before the start of every
round. The human also possesses a special ability,
which can be activated with a separate key. Once activated, the ability works for 5 turns,
after which it is automatically deactivated. After deactivation, the ability cannot be activated
for the next 5 turns. 

The simulation is initiated with several instances of every kind of
organism already placed in the game world. The program window includes a text box
for displaying messages about the results of fights between animals, consumption of plants
and other events occurring inside the simulated world.
The game ends, when the human player dies or when the map is full.

### Description of animal classes

| animal | strength | initiative | action | collision |
| --- | --- | --- | --- | --- | 
| wolf | 9 | 5 | default for Animal | default for Animal |
| sheep | 4 | 4 | default for Animal | default for Animal |
| fox | 3 | 7 | Has good sense of smell: fox will never move to a cell occupied by a stronger organism | default for Animal |
| turtle | 2 | 1 | Has 75% chance to stay in the same place | Reflects attacks of animal with strength less than 5. Attacker will return to the previous cell. |
| antelope | 4 | 4 | Has wider range of movement - 2 fields instead of 1. | Has 50% chance to escape from fight. In such case it moves to a free neighbouring cell. |
| cyber-sheep | 11 | 4 | Its main goal is the extermination of Sosnowsky's hogweed. It always moves towards the closes hogweed and tries to eat it. If there are no Sosnowsky's hogweeds, it behaves like a normal sheep. | Eats Sosnowsky's hogweed. |
