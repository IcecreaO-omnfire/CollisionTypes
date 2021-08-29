import GlobalVariables
import CharacterCollisionNode
class GameSetup():
    def __init__(self):
        self.customcollisions={}
        self.game=GlobalVariables.ShowBase()
        self.game.cTrav=GlobalVariables.CollisionTraverser()
        self.queuegame=GlobalVariables.CollisionHandlerQueue()
        taskMgr.doMethodLater(0.01,self.collisiontraverse,"CollisionTraverse")
    
    def collisiontraverse(self,task):
        self.game.cTrav.traverse(render)
        for each in self.game.cTrav.getColliders():
            try:
                collisionnode=self.customcollisions[each.node()]
                if isinstance(collisionnode,CharacterCollisionNode.CharacterCollisionNode):
                    collisionnode.model.setZ(collisionnode.model,-0.1)
            except Exception as exception:
                pass
        self.game.cTrav.showCollisions(render)
        if len(self.queuegame.entries)>0:
            for each in self.queuegame.entries:
                collisiontype=None
                fromnodepath=each.getFromNodePath()


                try:
                    if isinstance(self.customcollisions[fromnodepath.node()],CharacterCollisionNode.CharacterCollisionNode):
                        collisiontype=self.customcollisions[fromnodepath.node()]
                        #print(type(self.customcollisions[fromnodepath.node()]))
                        if collisiontype.isghost==True:
                            print("Ghosting")
                        else:
                            fromnodepath.getParent().setZ(fromnodepath.getParent(),each.getSurfacePoint(fromnodepath.getParent()).z+.9)   
                        

                except Exception as exception:
                    print(exception)
        
        return task.again