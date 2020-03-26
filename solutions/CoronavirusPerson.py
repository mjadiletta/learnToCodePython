import numpy as np
from solutions.graphics import *

CHANCE_OF_HEALTHY = 90  # 90% chance person is initialized to healthy
SPEED = 1

class Person:
    def __init__(self, win, x, y, radius):
        self.win = win
        self.x = x
        self.y = y
        self.dx = None
        self.dy = None
        self.radius = radius
        self.PD = radius*2
        self.SEPARATION_DISTANCE = self.PD**2
        self.speed = SPEED
        self.time_sick = None
        self.body = Circle(Point(self.x, self.y), radius)
        condition = np.random.randint(0, 100)
        if condition < CHANCE_OF_HEALTHY:
            self.condition = "healthy"
            self.body.setFill("MistyRose2")
        else:
            self.condition = "sick"
            self.body.setFill("firebrick3")
            self.time_sick = 0
        self.body.draw(win)
        self.initializeDirection()

    def move(self):
        self.x += self.dx*self.speed
        self.y += self.dy*self.speed
        self.body.move(self.dx*self.speed, self.dy*self.speed)

    def initializeDirection(self):
        x_dir = np.random.randint(-100, 100)
        y_dir = np.random.randint(-100, 100)

        normalizing_factor = np.sqrt(x_dir**2 + y_dir**2)
        self.dx = x_dir/normalizing_factor
        self.dy = y_dir/normalizing_factor

    def normalize(self, dx, dy):
        mag = np.sqrt(dx ** 2 + dy ** 2)
        return dx / mag, dy / mag

    def bouncePeople(self, people):
        p = self
        for p2 in people:
            dx = p2.x - p.x
            dy = p2.y - p.y
            if dx < self.PD or dy < self.PD:
                mag = dx ** 2 + dy ** 2
                if mag <= self.SEPARATION_DISTANCE:
                    mag = np.sqrt(mag)
                    vec_xp1 = dx / mag  # starting at p1
                    vec_yp1 = dy / mag  # starting at p1
                    vec_xp2 = -1 * dx / mag  # starting at p2
                    vec_yp2 = -1 * dy / mag  # starting at p2

                    swap1 = False
                    swap2 = False
                    if np.arccos(p.dx * vec_xp1 + p.dy * vec_yp1) * 180 / np.pi > 90:
                        swap1 = True
                    if np.arccos(p2.dx * vec_xp2 + p2.dy * vec_yp2) * 180 / np.pi > 90:
                        swap2 = True

                    dx, dy = self.normalize(vec_xp1 + p.dx, vec_yp1 + p.dy)

                    if (np.abs(dx) > np.abs(vec_xp1)):
                        vec_xp1, vec_yp1 = vec_yp1, vec_xp1 * -1
                    else:
                        vec_xp1, vec_yp1 = vec_yp1 * -1, vec_xp1

                    dx, dy = self.normalize(vec_xp2 + p.dx, vec_yp2 + p.dy)
                    if (np.abs(dx) > np.abs(vec_xp2)):
                        vec_xp2, vec_yp2 = vec_yp2, vec_xp2 * -1
                    else:
                        vec_xp2, vec_yp2 = vec_yp2 * -1, vec_xp2

                    if swap1:
                        p.dx, vec_xp1 = vec_xp1, p.dx
                        p.dy, vec_yp1 = vec_yp1, p.dy

                    if swap2:
                        p2.dx, vec_xp2 = vec_xp2, p2.dx
                        p2.dy, vec_yp2 = vec_yp2, p2.dy

                    p.bounceWall(vec_xp1, vec_yp1)
                    p2.bounceWall(vec_xp2, vec_yp2)
                    return p2
    def setFill(self, c):
        self.body.setFill(c)

    def bounceWall(self, colision_vector_x, colision_vector_y):  # takes the direction of the wall it should bounce off of
        dot = (self.dx * colision_vector_x + self.dy * colision_vector_y)
        dc_x = dot * colision_vector_x
        dc_y = dot * colision_vector_y

        ortho_x = colision_vector_y
        ortho_y = -1 * colision_vector_x
        dot = (self.dx * ortho_x + self.dy * ortho_y)
        do_x = -1 * dot * ortho_x
        do_y = -1 * dot * ortho_y

        self.dx = dc_x + do_x
        self.dy = dc_y + do_y
