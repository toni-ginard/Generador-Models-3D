#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Figures.Figure import Figure
from Random.Color import *


class Background:

    back = Figure()
    bottom = Figure()
    left = Figure()
    right = Figure()

    def __init__(self, back=Figure(), bottom=Figure(), left=Figure(), right=Figure()):
        self.back = back
        self.bottom = bottom
        self.left = left
        self.right = right

    def set_background(self):
        """ Sets a static background. """
        x_rand = random.uniform(-2, 2)
        y_rand = random.uniform(-2, 1)
        background_color = get_background_color()

        self.back.set_figure([-1.0 + x_rand, 3.0 + y_rand, -10.0], [16.0, 18.0, 10.0], background_color, 0, 0)
        self.bottom.set_figure([-1.0 + x_rand, -5.0 + y_rand, -10.0], [16.0, 18.0, 10.0], background_color, 90, 0)
        self.left.set_figure([-7.0 + x_rand, 3.0 + y_rand, -10.0], [16.0, 18.0, 10.0], background_color, 0, 90)
        self.right.set_figure([7.0 + x_rand, 3.0 + y_rand, -10.0], [16.0, 18.0, 10.0], background_color, 0, 90)

    def draw_background(self, plane, shader, view, projection, vao):
        """ Draws the background for the scene, representing the rooms' walls.

        :param plane: object to draw the planes.
        :param shader: figure's shader object.
        :param view: camera.
        :param projection: projection perspective matrix.
        :param vao: vertex array object.
        """
        plane.draw(shader, view, projection, self.back, vao)
        plane.draw(shader, view, projection, self.bottom, vao)
        plane.draw(shader, view, projection, self.left, vao)
        plane.draw(shader, view, projection, self.right, vao)
