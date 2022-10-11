from collections import namedtuple
from numpy import np
import math

x,y = range(2)

def convertToRadians(angle):
    return angle * float(math.pi) / 180.0

def getRotationMatrix(angle):
    return np.matrix([(math.cos(angle), -math.sin(angle)), (math.sin(angle), math.cos(angle))])

class RigidBody: 
    position = np.array([0,0])
    velocity = np.array([0,0])
    forces = np.array([0,0])
    mass: float
    angle: float
    angularVelocity : np.array([0,0])
    torque: float
    inertia: float
    size = np.array([0,0])

    def __init__(self):
        self.mass = 1.
        self.inertia = 1.

    def __init__(self, size, mass):
        self.size = size
        self.mass = mass
        halfsize = self.size / 2
        self.inertia = (halfsize[x] * halfsize[x]) * (halfsize[y] * halfsize[y]) * self.mass

    def getLocalVectorInWorldCoords(self, vector) :
        rotationMatrix = getRotationMatrix(self.angle)
        newVector = vector * rotationMatrix
        return newVector

    def getLocalVectorInWorldCoords(self, vector) :
        rotationMatrix = getRotationMatrix(-self.angle)
        newVector = vector * rotationMatrix
        return newVector    
    
    def getHalfSize(self):
        return self.size / 2

    def setPosition(self, position, angle) :
        self.position = position
        self.angle = angle

    def updateRigidBodyInfo(self, timeStep) :
        acceleration += self.forces / self.mass
        velocity += acceleration  * timeStep
        position += velocity  * timeStep
        self.forces = np.array([0,0])

        angularAcceleration = self.torque / self.inertia
        angularVelocity = angularAcceleration * timeStep
        angularAcceleration = angularVelocity * timeStep
        self.torque = 0
