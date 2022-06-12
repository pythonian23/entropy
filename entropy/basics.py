import numpy as np


class Vector3(np.ndarray):
    def __init__(self, x, y, z):
        super.__init__()


class Point(Vector3):
    ...


class Velocity(Vector3):
    ...


class Acceleration(Vector3):
    def apply(self, dt: float) -> Velocity:
        return Velocity(self*dt)


class Force(Vector3):
    def apply(self, mass, dt):


