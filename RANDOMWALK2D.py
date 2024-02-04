

# Python code for 2D random walk.
import numpy
import pylab
import random
import matplotlib.pyplot as plt



class Cell:
    def __init__(self, mytype, trajectory, stepspawn):
        self.mytype = mytype
        self.trajectory = trajectory

    def settype(self,mytype):
        self.mytype = mytype

    def settrajectory(self,trajectory):
        self.trajectory=trajectory

    def setstepspawn(self, stepspawn):
        self.stepspawn = stepspawn

    def getstepspawn(self):
        return self.stepspawn




 
# z initial starting point, n steps, k number of walkers, vals to decide the direction
w = 10
z = 10
n = 100
k = 10

vals = []
x = []
y = []
coord = []
for i in range (0,k):
    coord.append([])


#Creating Array for each Walker and their respective movement decision value
#ensuring that they do not start at the same position
for i in range(1, k+1):
    myval = f"val{i}"
    locals()[myval] = i
    vals.append(locals()[myval])
    cell=f"c{i}"
    locals()[cell] = Cell(1,0,-1)
    myx = f"x{i}"
    myy = f"y{i}"
    locals()[myx] = numpy.zeros(n)
    locals()[myy] = numpy.zeros(n)
    locals()[myx][0] = random.randint(-z,z)
    locals()[myy][0] = random.randint(-z,z)
    locals()[cell].settrajectory([locals()[myx],locals()[myy]])
    x.append(locals()[myx][0])
    y.append(locals()[myy][0])
    coord[i-1] = [x[i-1],y[i-1]]
    if i%2==0:
        locals()[cell].settype(0)
    if i > 1:
        while [x[i-1],y[i-1]] in coord[0:(i-1)]:
            locals()[myx][0] = random.randint(-z,z)
            locals()[myy][0] = random.randint(-z,z)
            x[i-1] = locals()[myx][0]
            y[i-1] = locals()[myy][0]
            coord[i-1] = [x[i-1],y[i-1]]
            
#Walking so that two walkers cant occupy one field
for i in range(1, n):
    for j in range (1, k+1):
        myx = f"x{j}"
        myy = f"y{j}"
        cell = f"c{j}"
        newcell = f"c{k+1}"
        newx = f"x{k+1}"
        newy = f"y{k+1}"
        vals[j-1] = random.randint(1,4)

        

        
        if vals[j-1] == 1:
            if i%8==0 and locals()[cell].mytype == 0:
                k = k+1
                locals()[newcell] = Cell(0,0,i)
                locals()[newcell].settype(0)
                locals()[newx] = numpy.zeros(n)
                locals()[newy] = numpy.zeros(n)
                locals()[newcell].setstepspawn(i)
                newval = random.randint(1,4)
                vals.append(newval)


                
                if newval == 1:
                    locals()[newx][i] =  locals()[myx][i - 1] + 1
                    locals()[newy][i] =  locals()[myy][i - 1]
                    locals()[newcell].settrajectory([locals()[newx],locals()[newy]])
                    x.append(locals()[newx][i])
                    y.append(locals()[newy][i])
                    check = k-1
                    while [x[k-1],y[k-1]] in coord:
                        del locals()[newcell]
                        del locals()[newy]
                        del locals()[newx]
                        x.pop()
                        y.pop()
                        k = k-1
                        break
                    if check == k-1:
                        coord.append([x[k-1],y[k-1]])



                
                elif newval == 2:
                    locals()[newx][i] =  locals()[myx][i - 1] - 1
                    locals()[newy][i] =  locals()[myy][i - 1]
                    locals()[newcell].settrajectory([locals()[newx],locals()[newy]])
                    x.append(locals()[newx][i])
                    y.append(locals()[newy][i])
                    check = k-1
                    while [x[k-1],y[k-1]] in coord:
                        del locals()[newcell]
                        del locals()[newy]
                        del locals()[newx]
                        x.pop()
                        y.pop()
                        k = k-1
                        break
                    if check == k-1:
                        coord.append([x[k-1],y[k-1]])


                    
                elif newval == 3:
                    locals()[newx][i] =  locals()[myx][i - 1]
                    locals()[newy][i] =  locals()[myy][i - 1] + 1
                    locals()[newcell].settrajectory([locals()[newx],locals()[newy]])
                    x.append(locals()[newx][i])
                    y.append(locals()[newy][i])
                    check = k-1
                    while [x[k-1],y[k-1]] in coord:
                        del locals()[newcell]
                        del locals()[newy]
                        del locals()[newx]
                        x.pop()
                        y.pop()
                        k = k-1
                        break
                    if check == k-1:
                        coord.append([x[k-1],y[k-1]])

                else:
                    locals()[newx][i] =  locals()[myx][i - 1]
                    locals()[newy][i] =  locals()[myy][i - 1] - 1
                    locals()[newcell].settrajectory([locals()[newx],locals()[newy]])
                    x.append(locals()[newx][i])
                    y.append(locals()[newy][i])
                    check = k-1
                    while [x[k-1],y[k-1]] in coord:
                        del locals()[newcell]
                        del locals()[newy]
                        del locals()[newx]
                        x.pop()
                        y.pop()
                        k = k-1
                        break
                    if check == k-1:
                        coord.append([x[k-1],y[k-1]])
            repx=0
            repy=0
            locals()[myx][i] = locals()[myx][i - 1] + 1
            locals()[myy][i] = locals()[myy][i - 1]
            x[j-1] = locals()[myx][i]
            y[j-1] = locals()[myy][i]
            """
            while [x[j-1],y[j-1]] in coord[0:(j-1)] and repx < 10:
                repx = repx + 1
                locals()[myx][i] =locals()[myx][i]  + random.randint(-1,1)
                x[j-1] = locals()[myx][i]
                coord[j-1] = [x[j-1],y[j-1]]
            while [x[j-1],y[j-1]] in coord[0:(j-1)] and repy < 10:
                repy = repy + 1
                locals()[myy][i] =locals()[myy][i] + random.randint(-1,1)
                y[j-1] = locals()[myy][i]
                coord[j-1] = [x[j-1],y[j-1]] """
            while [x[j-1],y[j-1]] in coord:
                locals()[myx][i] = locals()[myx][i - 1]-1
                locals()[myy][i] = locals()[myy][i - 1]
                x[j-1] = locals()[myx][i]
                y[j-1] = locals()[myy][i]
                coord[j-1] = [x[j-1],y[j-1]]
                break
            coord[j-1] = [x[j-1],y[j-1]]


            
        elif vals[j-1] == 2:
            repx=0
            repy=0
            locals()[myx][i] = locals()[myx][i - 1] - 1
            locals()[myy][i] = locals()[myy][i - 1]
            x[j-1] = locals()[myx][i]
            y[j-1] = locals()[myy][i]
            """
            while [x[j-1],y[j-1]] in coord[0:(j-1)] and repx < 10:
                repx = repx + 1
                locals()[myx][i] = locals()[myx][i] + random.randint(-1,1)
                x[j-1] = locals()[myx][i]
                coord[j-1] = [x[j-1],y[j-1]]
            while [x[j-1],y[j-1]] in coord[0:(j-1)] and repy < 10:
                repy = repy + 1
                locals()[myy][i] =locals()[myy][i] + random.randint(-1,1)
                y[j-1] = locals()[myy][i]
                coord[j-1] = [x[j-1],y[j-1]] """
            
            while [x[j-1],y[j-1]] in coord:
                locals()[myx][i] = locals()[myx][i - 1]+1
                locals()[myy][i] = locals()[myy][i - 1]
                x[j-1] = locals()[myx][i]
                y[j-1] = locals()[myy][i]
                coord[j-1] = [x[j-1],y[j-1]]
                break
            coord[j-1] = [x[j-1],y[j-1]]

        
            
        elif vals[j-1] == 3:
            repx=0
            repy=0
            locals()[myx][i] = locals()[myx][i - 1]
            locals()[myy][i] = locals()[myy][i - 1] + 1
            x[j-1] = locals()[myx][i]
            y[j-1] = locals()[myy][i]
            """
            while [x[j-1],y[j-1]] in coord[0:(j-1)] and repx < 10:
                repx = repx + 1
                locals()[myx][i] =locals()[myx][i]  + random.randint(-1,1)
                x[j-1] = locals()[myx][i]
                coord[j-1] = [x[j-1],y[j-1]]
            while [x[j-1],y[j-1]] in coord[0:(j-1)] and repy < 10:
                repy = repy + 1
                locals()[myy][i] =locals()[myy][i] + random.randint(-1,1)
                y[j-1] = locals()[myy][i]
                coord[j-1] = [x[j-1],y[j-1]]"""
            while [x[j-1],y[j-1]] in coord:
                locals()[myx][i] = locals()[myx][i - 1]
                locals()[myy][i] = locals()[myy][i - 1] - 1
                x[j-1] = locals()[myx][i]
                y[j-1] = locals()[myy][i]
                coord[j-1] = [x[j-1],y[j-1]]
                break
            coord[j-1] = [x[j-1],y[j-1]]

       
            
        else:
            repx=0
            repy=0
            locals()[myx][i] = locals()[myx][i - 1]
            locals()[myy][i] = locals()[myy][i - 1] - 1
            x[j-1] = locals()[myx][i]
            y[j-1] = locals()[myy][i]
            """
            while [x[j-1],y[j-1]] in coord[0:(j-1)] and repx < 10:
                repx = repx + 1
                locals()[myx][i] = locals()[myx][i] + random.randint(-1,1)
                x[j-1] = locals()[myx][i]
                coord[j-1] = [x[j-1],y[j-1]]
            while [x[j-1],y[j-1]] in coord[0:(j-1)] and repy < 10:
                repy = repy + 1
                locals()[myy][i] =locals()[myy][i] + random.randint(-1,1)
                y[j-1] = locals()[myy][i]
                coord[j-1] = [x[j-1],y[j-1]]
                 """
            while [x[j-1],y[j-1]] in coord:
                locals()[myx][i] = locals()[myx][i - 1]
                locals()[myy][i] = locals()[myy][i - 1] + 1
                x[j-1] = locals()[myx][i]
                y[j-1] = locals()[myy][i]
                coord[j-1] = [x[j-1],y[j-1]]
                break
            coord[j-1] = [x[j-1],y[j-1]]

                
            
"""        #Plotting
    pylab.title("Random Walk ($n = " + str(n) + "$ steps" + ", $k = " + str(k) + "$ walkers)")
    print(coord)
    for b in range(1, k+1):
        myx = f"x{b}"
        myy = f"y{b}"
        thatx = locals()[myx]
        thaty = locals()[myy]
        #pylab.scatter(thatx,thaty)
        pylab.plot(thatx[0],thaty[0],"bo", color = "red")
        pylab.plot(thatx[i],thaty[i],"bo", color = "green")
    #pylab.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=600)
    pylab.show()"""

#Modification for plotting
for i in range (w+1,k+1):
    myx = f"x{i}"
    myy = f"y{i}"
    cell = f"c{i}"
    originstep = locals()[cell].getstepspawn()
    for j in range(0,originstep):
        locals()[myx] = numpy.delete(locals()[myx], 0)
        locals()[myy] = numpy.delete(locals()[myy], 0)



#Plotting
pylab.title("Random Walk ($n = " + str(n) + "$ steps" + ", $k = " + str(k) + "$ walkers)")
for b in range(1, k+1):
    myx = f"x{b}"
    myy = f"y{b}"
    thatx = locals()[myx]
    thaty = locals()[myy]
    pylab.plot(thatx,thaty)
    pylab.plot(thatx[0],thaty[0],"bo")
    pylab.plot(thatx[-1],thaty[-1],"bo",color = "red")
#pylab.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=600)
pylab.show()
        



