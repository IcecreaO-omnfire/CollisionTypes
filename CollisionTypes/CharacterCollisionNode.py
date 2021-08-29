import GlobalVariables
import xml
import xml.etree.ElementTree as xmlparse
class CharacterCollisionNode():
    def __init__(self,name,modelname,model,dataxml):
        self.collisionnode=GlobalVariables.CollisionNode(name)
        self.collisionnode.addSolid(GlobalVariables.CollisionBox(*model.getTightBounds()))
        self.isghost=False
        self.model=model
        for each in dataxml.getchildren():
            print(each)
            if each.tag=="ghost":
                self.isghost=True
