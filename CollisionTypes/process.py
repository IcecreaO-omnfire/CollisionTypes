import GlobalVariables
from GameSetup import *
from Character import *
game=GameSetup()

character1=Character1(game)
game.customcollisions[character1.collisiontype.collisionnode] =character1.collisiontype
block=loader.loadModel("Block.obj")
block.setTexture(loader.loadTexture("206.jpg"))
block.setCollideMask(GlobalVariables.BitMask32.allOn())
block.setScale(10)
block.reparentTo(render)
camera.setPos(0,10,0)
game.game.disableMouse()
camera.setHpr(-180,0,0)
camera.reparentTo(character1.model)
game.game.run()
