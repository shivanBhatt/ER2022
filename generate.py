import pyrosim.pyrosim as pyrosim

x,y,z = 1.5,0,1.5
length,width,height = 1,1,1
size=[length,width,height]

def Create_World():

    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube('box',[0,3,0.5],size)
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube('Torso',[x,y,z],size)
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube('BackLeg',[-0.5,0,-0.5],size)
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
    pyrosim.Send_Cube('FrontLeg',[0.5,0,-0.5],size)

    pyrosim.End()

Create_World()
Create_Robot()