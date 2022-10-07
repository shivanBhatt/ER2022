import pyrosim.pyrosim as pyrosim

x,y,z = 0,0,0.5
length,width,height = 1,1,1
size=[length,width,height]
pyrosim.Start_SDF("boxes.sdf")
for i in range(5):
    for j in range(5):
        size=[length,width,height]
        for k in range(10):
            name = 'Box'+str(i+1)+str(j+1)+str(k+1)
            pyrosim.Send_Cube(name, [x+i,y+j,z+k], size)
            size = [d*0.9 for d in size]    

        
    # print(size)
    # print(size[2]/2+z)
    # pyrosim.Send_Cube(name, [x,y,size[2]/2+z] , size)
    # z += size[2]
    # size = [d*0.9 for d in size]

pyrosim.End()
