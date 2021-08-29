import GlobalVariables
import xml
import xml.etree.ElementTree as xmlparse
import CharacterCollisionNode
class Character1():
    def __init__(self,game):
        self.eventsaccept=GlobalVariables.DirectObject.DirectObject()
        self.model=loader.loadModel("jack.egg")
        self.gameinstance=game
        datacharacter=open("xmlcharacter.xml","r")
        filetext=datacharacter.read()
        textdata=xmlparse.fromstring(filetext)
        xmldata=None
        for each in textdata:
            if each.tag=="character1":
                xmldata=each
                break
        self.collisiontype=CharacterCollisionNode.CharacterCollisionNode("CharacterCollision",self.model.getName(),self.model,xmldata)
        self.collisiontype.collisionnode.addSolid(GlobalVariables.CollisionBox(*self.model.getTightBounds()))
        self.collisionNodePath=self.model.attachNewNode(self.collisiontype.collisionnode)
        game.game.cTrav.addCollider(self.collisionNodePath,self.gameinstance.queuegame)
        self.model.reparentTo(render)
        self.collisionNodePath.show()
        
        self.eventsaccept.accept("a",self.moveleft,extraArgs=[1])
        self.eventsaccept.accept("d",self.moveright,extraArgs=[1])
        self.eventsaccept.accept("w",self.moveforward,extraArgs=[1])
        self.eventsaccept.accept("s",self.moveback,extraArgs=[1])
        self.eventsaccept.accept("space",self.jump,extraArgs=[3])
        #taskMgr.doMethodLater(0.1,self.jumptime,"Jumptime",appendTask=True)
        
            
    def jumptime(self,task):
        self.model.setZ(self.model,-0.1)
        return task.again
    
    ###############################
    ###############################

    def jump(self,movementspeed):
        self.relativePos(self.model,(0,0,1),movementspeed)

    ###############################
    ###############################    
    def moveleft(self,movementspeed):
        self.relativePos(self.model,(-1,0,0),movementspeed)

    ###############################
    ###############################
    def moveright(self,movementspeed):
        self.relativePos(self.model,(1,0,0),movementspeed)

    ###############################
    ###############################
    def moveback(self,movementspeed):
        self.relativePos(self.model,(0,-1,0),movementspeed)

    ###############################
    ###############################
    def moveforward(self,movementspeed):
        self.relativePos(self.model,(0,1,0),movementspeed)

    ###############################
    ###############################
    def relativePos(self,model,movedirection,relativemovement):
        model.setPos(model,movedirection[0]*relativemovement,movedirection[1]*relativemovement,movedirection[2]*relativemovement)
        
    ###############################
    ###############################