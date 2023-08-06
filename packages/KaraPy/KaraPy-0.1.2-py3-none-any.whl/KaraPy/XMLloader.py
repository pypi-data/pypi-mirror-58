import xml.etree.ElementTree as ET 
from KaraPy.KaraWorld import World
from KaraPy.Enums import Type, Move

def LoadWorldFile(source, size):
    data = open(source)
    tree = ET.parse(data)
    root = tree.getroot()

    sizex = int(root.attrib["sizex"]) 
    sizey = int(root.attrib["sizey"]) 

    sizexa = sizex * size 
    sizeya = sizey * size
    W = World(size, (sizexa,sizeya))
    W.build()
    
    T = root.find("XmlWallPoints")
    for tree in T.findall("XmlPoint"):
        x =  int(tree.attrib["x"])
        y = sizey - int(tree.attrib["y"]) -1
        W.Place(Type.Tree, (x,y))
    L = root.find("XmlPaintedfieldPoints")
    for leaf in L.findall("XmlPoint"):
        x = int(leaf.attrib["x"])
        y = sizey - int(leaf.attrib["y"]) -1
        W.Place(Type.Leaf, (x,y))
    K = root.find("XmlKaraList")
    k = K.find("XmlKara")
    x = int(k.attrib["x"])
    y = sizey - int(k.attrib["y"]) -1
    f = k.attrib["direction"]
    
    W.Place(Type.Kara, (x,y))

    if f == "0":
        W.Move(Move.TurnLeft)
    if f == "1":
        W.Move(Move.TurnLeft)
        W.Move(Move.TurnLeft)
    if f == "2":
        W.Move(Move.TurnRight)
    return W