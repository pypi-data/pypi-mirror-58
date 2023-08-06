import turtle, time
from KaraPy.Enums import *

class World(object):
    global height
    global width
    global mesh
    global world
    global Kara
    global facing
    global KaraPos
    global speed
    global worldType
    global availableT
    global title
    global States
    
    def getKara(self):
        global Kara
        return Kara
    
    def getFacing(self):
        global facing
        return facing
    
    def getKaraPos(self):
        global KaraPos
        return KaraPos
    
    def getSize(self):
        global width, height, mesh
        return (int(width/mesh), int(height/mesh))

    def __init__(self,  meshSize, size, sp = 0.5, _title=""):
        global height, width, mesh, world, Kara, speed, worldType, availableT, KaraPos, title, States
        height, width = size
        height = height*50 * meshSize
        width = width*50 * meshSize
        mesh =  1 * 50 * meshSize 
        world = []
        worldType = []
        availableT = []
        title = _title
        States = []
        Kara = False
        KaraPos = (0,0)
        if sp >= 0 and sp <= 1:
            speed = 1.1 - sp 
        else:
            print("Speed value must be between 0 and 1! \nDefaulted it to 0.5")
            speed = 0.5

    def build(self):
        global canvas, height, width, t, mesh, world, speed, worldType, title
        canvas = turtle.Screen()
        #canvas.bgpic("logo.gif")
        canvas.setup(width=width + 100, height=height + 100)
        canvas.screensize(width , height)
        canvas.bgcolor("lightgreen")
        canvas.title("Kara Python version 0.2 " + title )
        t = turtle.Turtle()
        t.speed(10)
        t.hideturtle()
        t.penup()
        t.goto( width/2 * -1, height/2 * -1 )
        t.pendown()
        t.goto(width/2, height/2 * -1)
        t.goto(width/2, height/2)
        t.goto(width/2 * -1, height/2)
        t.goto(width/2 * -1, height/2 * -1)
        self.drawMesh()
        for w in range(int(width/mesh)):
            world.insert(w, [])
            worldType.insert(w, [])
            for h in range(int(height/mesh)):
                world[w].insert(h,None)  
                worldType[w].insert(h, "N")
        time.sleep(speed)
                
    def drawMesh(self):
        global t, width, height, mesh
        t.speed(1000)
        w = 0
        while w < width/2:
            t.setx(t.position()[0] + mesh)
            t.sety(t.position()[1] * -1)
            w = w + mesh/2
        t.penup()
        t.goto(width/2 * -1, height/2 * -1)
        t.pendown()

        h = 0
        while h < height/2:
            t.sety(t.position()[1] + mesh)
            t.setx(t.position()[0] * -1)
            h = h + mesh/2 

    def Place(self, tile, pos):
        global width, height, world, mesh, Kara, facing, KaraPos, speed, worldType, KaraObj
        x,y = pos
        if x < width/mesh and y < height/mesh and x >= 0 and y >= 0 :  
            if world[x][y] == None:
                xa = x * mesh - width/2  + mesh/2
                ya = y * mesh - height/2 + mesh/2
        
                if tile == Type.Tree:
                    t = turtle.Turtle()
                    t.shape("square")
                    t.shapesize((mesh - 10) /25)
                    t.color("brown")
                    t.penup()
                    t.speed(100)
                    t.goto(xa, ya)
                    world[x][y] = t
                    worldType[x][y] = "T"
                if tile == Type.Leaf:
                    t = turtle.Turtle()
                    t.shape("circle")
                    t.shapesize((mesh - 10) /25)
                    t.color("darkgreen")
                    t.penup()
                    t.speed(100)
                    t.goto(xa, ya)
                    world[x][y] = t
                    worldType[x][y] = "L"
                if tile == Type.Kara:
                    if not Kara:
                        t = turtle.Turtle()
                        t.shape("turtle")
                        t.shapesize((mesh - 10) /30)
                        t.color("#750000")
                        t.penup()
                        t.hideturtle()
                        t.goto(xa, ya)
                        t.showturtle()
                        facing = Facing.Right
                        KaraPos = (x,y)
                        Kara = True
                        KaraObj = t
                        
                    else:
                        print("There is already one Kara in the world")
            elif worldType[x][y] == "L" and tile == Type.Kara:
                xa = x * mesh - width/2  + mesh/2
                ya = y * mesh - height/2 + mesh/2
                if not Kara:
                    t = turtle.Turtle()
                    t.shape("turtle")
                    t.shapesize((mesh - 10) /30)
                    t.color("red")
                    t.penup()
                    t.hideturtle()
                    t.goto(xa, ya)
                    t.showturtle()
                    facing = Facing.Right
                    KaraPos = (x,y)
                    Kara = True
                    KaraObj = t
                else:
                    print("There is already one Kara in the world")
            else:
                print("There is already an Object")
        else:
            print("Position out of Grid")

    def getWorldArray(self):
        global worldType
        return worldType

    def Move(self, move):
        global Kara, facing, world, KaraPos , speed, width, height, mesh, worldType, KaraObj, availableT
        x,y = KaraPos
        if Kara:
            if move == Move.Go:
                if facing == Facing.Right:
                    if not (x == width/mesh -1):
                        o = worldType[x + 1][y]
                        if o == "T":
                            print("Kara can not walk there is a tree in front of her.")
                        else:
                            xa = (x +1) * mesh - width/2  + mesh/2
                            ya = y * mesh - height/2 + mesh/2
                            KaraPos = (x+1 , y)
                            KaraObj.goto(xa, ya)
                    else:
                        o = worldType[0][y]
                        if o == "T":
                            print("Kara can not walk there is a tree in front of her.")
                        else:
                            xa = 0 * mesh - width/2  + mesh/2
                            ya = y * mesh - height/2 + mesh/2
                            KaraPos = (0 , y)
                            KaraObj.goto(width/2 , ya)
                            KaraObj.hideturtle()
                            KaraObj.goto(width/2 * -1, ya)
                            KaraObj.showturtle()
                            KaraObj.goto(xa, ya)

                if facing == Facing.Left:
                    if not (x == 0):
                        o = worldType[x - 1][y]
                        if o == "T":
                            print("Kara can not walk there is a tree in front of her.")
                        else:
                            xa = (x - 1) * mesh - width/2  + mesh/2
                            ya = y * mesh - height/2 + mesh/2
                            KaraPos = (x - 1 , y)
                            KaraObj.goto(xa, ya)
                    else:
                        o = worldType[int(width/mesh - 1)][y]
                        if o == "T":
                            print("Kara can not walk there is a tree in front of her.")
                        else:
                            xa = int(width/mesh - 1) * mesh - width/2  + mesh/2
                            ya = y * mesh - height/2 + mesh/2
                            KaraPos = (int(width/mesh - 1) , y)
                            KaraObj.goto(width/2 * -1, ya)
                            KaraObj.hideturtle()
                            KaraObj.goto(width/2, ya)
                            KaraObj.showturtle()
                            KaraObj.goto(xa, ya)

                if facing == Facing.Up:
                    if not (y == height/mesh -1):
                        o = worldType[x][y + 1]
                        if o == "T":
                            print("Kara can not walk there is a tree in front of her.")
                        else:
                            xa = x * mesh - width/2  + mesh/2
                            ya = (y + 1) * mesh - height/2 + mesh/2
                            KaraPos = (x , y + 1)
                            KaraObj.goto(xa, ya)
                    else:
                        o = worldType[x][0]
                        if o == "T":
                            print("Kara can not walk there is a tree in front of her.")
                        else:
                            xa = x * mesh - width/2  + mesh/2
                            ya = 0 * mesh - height/2 + mesh/2
                            KaraPos = (x , 0)
                            KaraObj.goto(xa, height/2)
                            KaraObj.hideturtle()
                            KaraObj.goto(xa, height/2 * -1)
                            KaraObj.showturtle()
                            KaraObj.goto(xa, ya)

                if facing == Facing.Down:
                    if not (y == 0):
                        o = worldType[x][y - 1]
                        if o == "T":
                            print("Kara can not walk there is a tree in front of her.")
                        else:
                            xa = x * mesh - width/2  + mesh/2
                            ya = (y - 1) * mesh - height/2 + mesh/2
                            KaraPos = (x , y - 1)
                            KaraObj.goto(xa, ya)
                    else:
                        o = worldType[x][int(height/mesh -1)]
                        if o == "T":
                            print("Kara can not walk there is a tree in front of her.")
                        else:
                            xa = x * mesh - width/2  + mesh/2
                            ya = int(height/mesh - 1) * mesh - height/2 + mesh/2
                            KaraPos = (x , int(height/mesh - 1))
                            KaraObj.goto(xa, height/2 * -1)
                            KaraObj.hideturtle()
                            KaraObj.goto(xa, height/2)
                            KaraObj.showturtle()
                            KaraObj.goto(xa, ya)

            if move == Move.TurnLeft:
                if facing == Facing.Right:
                    facing = Facing.Up
                    t = KaraObj
                    t.left(90)
                elif facing == Facing.Left:
                    facing = Facing.Down
                    t = KaraObj 
                    t.left(90)
                elif facing == Facing.Up:
                    facing = Facing.Left
                    t = KaraObj
                    t.left(90)
                elif facing == Facing.Down:
                    facing = Facing.Right
                    t = KaraObj
                    t.left(90)

            if move == Move.TurnRight:
                if facing == Facing.Right:
                    facing = Facing.Down
                    t = KaraObj
                    t.right(90)
                elif facing == Facing.Left:
                    facing = Facing.Up
                    t = KaraObj 
                    t.right(90)
                elif facing == Facing.Up:
                    facing = Facing.Right
                    t = KaraObj
                    t.right(90)
                elif facing == Facing.Down:
                    facing = Facing.Left
                    t = KaraObj
                    t.right(90)
        
            if move == Move.Up:
                o = worldType[x][y]
                if o == "L":
                    t = world[x][y]
                    t.hideturtle()
                    availableT.append(t)
                    world[x][y] = None
                    worldType[x][y] = "N"
                else:
                    print("Kara kann kein Kleeblat aufheben wo keins Liegt.")
        
            if move == Move.Down:
                o = worldType[x][y]
                if not o == "L":
                    xa = x * mesh - width/2  + mesh/2
                    ya = y * mesh - height/2 + mesh/2
                    if availableT.__len__() > 0:
                        t = availableT[0]
                        availableT.remove(t)
                        t.goto(xa, ya)
                        t.showturtle()
                        world[x][y] = t
                        worldType[x][y] = "L"
                    else:
                        t = turtle.Turtle()
                        t.hideturtle()
                        t.shape("circle")
                        t.shapesize((mesh - 10) /25)
                        t.color("darkgreen")
                        t.penup()
                        t.goto(xa, ya)
                        t.showturtle()
                        world[x][y] = t
                        worldType[x][y] = "L"
                    KaraObj.goto(xa,ya)
                else:
                    print("Kara kann kein Kleeblatt hinlegen wo bereits eins liegt.")
        else:
            print("There is no Kara in the Wolrd")
        time.sleep(speed)

    def setSpeed(self, sp):
        global speed
        if sp >= 0 and sp <= 1:
            	speed = 1.1 - sp
        else:
            print("Speed value must be between 0 and 1! \nDefaulted it to 0.5")
            speed = 0.5
        
    def getSensor(self, sensor):
        global KaraPos, worldType, facing
        x,y = KaraPos
        if sensor == Sensor.L:
            o = worldType[x][y]
            return o == "L"
        if sensor == Sensor.TF:
            if facing == Facing.Right:
                o = worldType[x +1][y]
                return o == "T"
            if facing == Facing.Left:
                o = worldType[x -1][y]
                return o == "T"
            if facing == Facing.Up:
                o = worldType[x][y + 1]
                return o == "T"
            if facing == Facing.Down:
                o = worldType[x][y -1]
                return o == "T"
        if sensor == Sensor.TL:
            if facing == Facing.Right:
                o = worldType[x][y + 1]
                return o == "T"
            if facing == Facing.Left:
                o = worldType[x][y -1]
                return o == "T"
            if facing == Facing.Up:
                o = worldType[x + 1][y]
                return o == "T"
            if facing == Facing.Down:
                o = worldType[x -1][y]
                return o == "T" 
        if sensor == Sensor.TR:
            if facing == Facing.Right:
                o = worldType[x -1][y]
                return o == "T"
            if facing == Facing.Left:
                o = worldType[x +1][y]
                return o == "T"
            if facing == Facing.Up:
                o = worldType[x][y - 1]
                return o == "T"
            if facing == Facing.Down:
                o = worldType[x][y +1]
                return o == "T"

    def setBrain(self, _States):
        global States
        States = _States
        
    def Start(self):
        global States
        start = None
        for state in States:
            if state.getStart():
                start = state
        if not start == None:
            nextstate = start
            while not nextstate == None:
                nextstate = execute(nextstate)
        else:
            print("You must define a Start State!")
            return

    def execute(self, state):
        ts = state.getTransitions()
        ft = None
        for t in ts:
            ks = t.getConditions()
            this = True
            for k in ks:
                result = self.getSensor(k[0]) == k[1]
                if not result:
                    this = False
            if this:
                ft = t
        if not ft == None:
            out = ft.getOutput()
            for o in out:
                self.Move(o)
            return ft.getNextState()
        else:
            print("No Condition  matching!")
            return None

        return #next State

