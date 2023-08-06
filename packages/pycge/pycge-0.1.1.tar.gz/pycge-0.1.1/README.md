# PyCGE

pycge - or python colored game engine - is a 2d game engine made in python.

## Why pycge?

pycge is a game engine that uses colors and run perfectly in your terminal. This can be used by developers that need a more interactive system. Pycge can also be used as a menu system.

# DOCS
## installation

pycge will be available at [pip](https://pip.pypa.io/en/stable/)

# usage

first, let's create an empty game:
```
import pycge.pycge as pcg

dimention = [10, 10]

game = pcg.Game(dimention)
game.start()
```
feel free to experiment with variables and values.

Now let's add a character.
This is achieved by adding two things:
a layer and an actor.

a layer is a plane with the same dimention as the game board, if two actors with hitbox disabled collide on the same layer one will be overwritten, therefore it is important to have every actor that might collide on seperate layers.
a good layer system would be:
- background layer (a layer of static actors that you know wont be moved)
- player layer (a layer with the player which can roam around freely and interact with other actors on different layers)
- opponent layer (this layer can be used to hold other actors that necessarily wont be controlled by the player)

For now let's just keep it to one layer,
let's call it the player layer.
```
playerLayer = pcg.Layer(dimention)
game.addLayer(playerLayer, 5)
```
dimention is the variable we defined above containing the dimentions for the game board.

5 is the index of the layer. A layer with higher index will be prioritized over another layer with lower index. Since we only have one layer this value isn't important for now


if you run your pycge game now you wont notice any difference, that's because you can't see empty layers.
so let's add something to the layer
let's add a player.

```
player = pcg.Actor("blue")
player.place(4, 5, playerLayer)
```
The first line defines an actor.
the argument defines the color of the player. Here's a list of valid colors:
- grey
- red
- green
- yellow
- blue
- magenta
- cyan
- white

line #2 places the actor on x=4, y=5 and the layer is playerLayer.

If you now run our game you will see our blue player on the screen. But you can't control the player.

So let's map keys to make our player move.

First of all we need two more imports
```
import pycge.key as key
import pycge.examples as examples
```

the top import is a library that handles key structures
the bottom import contains examples (that is fully replacable) such as a class that moves the character up.

```
keyMapping = key.KeyStruct()

keyMapping.add("w", examples.up, player)
keyMapping.add("a", examples.left, player)
keyMapping.add("s", examples.down, player)
keyMapping.add("d", examples.right, player)
```
- the first argument is a str of one letter which is the key activating this function
- the second argument is a class returning a list of new x and y pos for this function. (if you are going to create your own class you have to have a var called self.val which is a list of two elements; x and y)
- the third and final argument is deciding what actor it should bind with that key.

We are not done yet.
All we need to do now is to tell the game to use this structure.
This is easy, modify the `game.start()` to something like this:
`game.start(keyMapping)`

That should be it!
if you have followed the tutorial correctly should have a movable character which you can color and a background you can resize.

full code:
```
import pycge.pycge as pcg
import pycge.key as key
import pycge.examples as examples

dimention = [10, 10]

game = pcg.Game(dimention)

playerLayer = pcg.Layer(dimention)
game.addLayer(playerLayer, 5)

player = pcg.Actor("blue")
player.place(4, 5, playerLayer)

keyMapping = key.KeyStruct()

keyMapping.add("w", examples.up, player)
keyMapping.add("a", examples.left, player)
keyMapping.add("s", examples.down, player)
keyMapping.add("d", examples.right, player)

game.start(keyMapping)
```

### examples

[racing cars example](https://pastebin.com/De39SY6a)

# LICENSE

remember to read the license:
"LICENSE"